from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagerViewSet, InternViewSet, AddressViewSet

router = DefaultRouter()
router.register(r'managers', ManagerViewSet)
router.register(r'interns', InternViewSet)
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]