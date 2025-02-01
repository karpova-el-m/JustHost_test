from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.constants import STATUS_CHOICES
from .models import VPS
from .serializers import VPSSerializer


class VPSViewSet(viewsets.ModelViewSet):
    """Вьюсет модели VPS."""
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ('cpu', 'ram', 'hdd', 'status')
    search_fields = ('^uid', 'cpu', 'ram', 'hdd')
    ordering_fields = ('uid', 'ram')
    ordering = ('uid',)

    @action(
        detail=True,
        methods=['patch'],
        url_path='change_status'
    )
    def change_status(self, request, pk=None):
        """Изменение статуса VPS."""
        vps = self.get_object()
        new_status = request.data.get('status')
        if new_status not in dict(STATUS_CHOICES):
            return Response(
                {"error": "Invalid status."},
                status=status.HTTP_400_BAD_REQUEST
            )
        vps.status = new_status
        vps.save()
        return Response({"status": "Status updated successfully."})
