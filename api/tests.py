from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import VPS

User = get_user_model()


class VPSTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.vps_data = {
            'cpu': 2,
            'ram': 4096,
            'hdd': 100,
            'status': 'stopped'
        }
        self.vps = VPS.objects.create(**self.vps_data)

    def test_create_vps_unauthorized(self):
        response = self.client.post('/api/vps/', self.vps_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_vps_authorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/vps/', self.vps_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_vps(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/vps/{self.vps.uid}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_status(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            f'/api/vps/{self.vps.uid}/change_status/',
            {'status': 'started'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vps.refresh_from_db()
        self.assertEqual(self.vps.status, 'started')

    def test_filter_vps(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/vps/?cpu=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_sort_vps(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/vps/?ordering=-cpu')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_search_vps(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/vps/?search={self.vps.uid}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
