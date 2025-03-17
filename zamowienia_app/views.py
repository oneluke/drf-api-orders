from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum

from .models import Klient, Produkt, Zamowienie, PozycjaZamowienia
from .serializers import KlientSerializer, ProduktSerializer, ZamowienieSerializer, PozycjaZamowieniaSerializer


# odczyt dla wszystkich, edycja tylko dla zalogowanych
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


# endpointy dostępne tylko dla zalogowanych
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def zestawienie_miesieczne(request):
    """
    Zwraca liczbę zamówień i łączną wartość zamówień dla każdego miesiąca.
    """
    dane = (
        Zamowienie.objects.annotate(miesiac=TruncMonth('data_zamowienia'))
        .values('miesiac')
        .annotate(
            liczba_zamowien=Count('id'),
            laczna_wartosc=Sum('pozycje__cena_sztuka') 
        )
        .order_by('miesiac')
    )
    return Response(dane)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def zamowienia_klienta(request, klient_id):
    """
    Zwraca listę zamówień dla danego klienta.
    """
    zamowienia = Zamowienie.objects.filter(klient_id=klient_id)
    serializer = ZamowienieSerializer(zamowienia, many=True)
    return Response(serializer.data)
