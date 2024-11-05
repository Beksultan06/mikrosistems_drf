from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserRegister, UserLoginSerializer

User = get_user_model()

class UserViewSet(CreateModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegister

    def get_serializer_class(self):
        """Выбор сериализатора в зависимости от выполняемого действия"""
        if self.action == 'register':
            return UserRegister
        elif self.action == 'login':
            return UserLoginSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        """Регистрация нового пользователя и выдача токена"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user).access_token
            return Response({"token": str(token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        """Вход пользователя и выдача токена"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = RefreshToken.for_user(user).access_token
            return Response({"token": str(token)}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='validate_token', permission_classes=[IsAuthenticated])
    def validate_token(self, request):
        """Проверка валидности токена"""
        return Response({"message": "Token is valid"}, status=status.HTTP_200_OK)