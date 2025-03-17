from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KlientViewSet, ProduktViewSet, ZamowienieViewSet, PozycjaZamowieniaViewSet

router = DefaultRouter()
router.register(r'klienci', KlientViewSet)
router.register(r'produkty', ProduktViewSet)
router.register(r'zamowienia', ZamowienieViewSet)
router.register(r'pozycje', PozycjaZamowieniaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
