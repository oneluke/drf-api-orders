from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Klient, Produkt, Zamowienie, PozycjaZamowienia
from .serializers import KlientSerializer, ProduktSerializer, ZamowienieSerializer, PozycjaZamowieniaSerializer

class KlientViewSet(viewsets.ModelViewSet):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProduktViewSet(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ZamowienieViewSet(viewsets.ModelViewSet):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PozycjaZamowieniaViewSet(viewsets.ModelViewSet):
    queryset = PozycjaZamowienia.objects.all()
    serializer_class = PozycjaZamowieniaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

