from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import VPS


class VPSTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vps_data = {
            'cpu': 2,
            'ram': 4096,
            'hdd': 100,
            'status': 'stopped'
        }
        self.vps = VPS.objects.create(**self.vps_data)

    def test_create_vps(self):
        url = reverse('api:vps-list')
        response = self.client.post(url, self.vps_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_vps(self):
        url = reverse('api:vps-detail', args=[self.vps.uid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_status(self):
        url = reverse('api:vps-change-status', args=[self.vps.pk])
        response = self.client.patch(url, {'status': 'started'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vps.refresh_from_db()
        self.assertEqual(self.vps.status, 'started')
