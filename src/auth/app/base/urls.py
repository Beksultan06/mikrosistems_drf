from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()
router.register("register", UserViewSet, basename='register')

urlpatterns = [
    
]

urlpatterns += router.urls