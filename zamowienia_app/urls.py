from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    KlientViewSet, ProduktViewSet, ZamowienieViewSet, PozycjaZamowieniaViewSet,
    zestawienie_miesieczne, zamowienia_klienta
)

router = DefaultRouter()
router.register(r'klienci', KlientViewSet)
router.register(r'produkty', ProduktViewSet)
router.register(r'zamowienia', ZamowienieViewSet)
router.register(r'pozycje', PozycjaZamowieniaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('zestawienie-miesieczne/', zestawienie_miesieczne, name='zestawienie-miesieczne'),
    path('zamowienia-klienta/<int:klient_id>/', zamowienia_klienta, name='zamowienia-klienta'),
]
