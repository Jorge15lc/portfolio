from rest_framework.views import APIView
from rest_framework.response import Response
from apps.main.models import Service
from ..serializers import ServiceSerializer

# ------------------------------------------------------------

class ServiceDetailView(APIView):
    def get(self, request, pk, format=None):
        service = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)