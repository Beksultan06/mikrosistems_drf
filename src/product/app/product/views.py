from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Product
from .serializers import ProductSerializer
import requests

class ProductViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_authentication_check(self, request):
        """Вспомогательный метод для проверки токена"""
        auth_token = request.headers.get("Authorization")
        auth_response = requests.get("http://auth_service:8000/validate_token/", headers={"Authorization": auth_token})
        if auth_response.status_code != 200:
            return False
        return True

    def perform_create(self, serializer):
        if not self.perform_authentication_check(self.request):
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        if not self.perform_authentication_check(self.request):
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer.save()

    def perform_destroy(self, instance):
        if not self.perform_authentication_check(self.request):
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        instance.delete()