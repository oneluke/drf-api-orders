from rest_framework import serializers
from .models import Klient, Produkt, Zamowienie, PozycjaZamowienia

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'

class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = '__all__'

class PozycjaZamowieniaSerializer(serializers.ModelSerializer):
    zamowienie = serializers.PrimaryKeyRelatedField(queryset=Zamowienie.objects.all())  # Dodaj możliwość wyboru zamówienia
    produkt = serializers.PrimaryKeyRelatedField(queryset=Produkt.objects.all()) 

    class Meta:
        model = PozycjaZamowienia
        fields = '__all__'

    class Meta:
        model = PozycjaZamowienia
        fields = '__all__'

class ZamowienieSerializer(serializers.ModelSerializer):
    klient = serializers.PrimaryKeyRelatedField(queryset=Klient.objects.all())
    pozycje = PozycjaZamowieniaSerializer(many=True, read_only=True)

    class Meta:
        model = Zamowienie
        fields = '__all__'
