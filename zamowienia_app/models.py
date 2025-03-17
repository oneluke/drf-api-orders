from django.db import models
from django.contrib.auth.models import User

class Klient(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefon = models.CharField(max_length=15, blank=True, null=True)
    data_dodania = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True, null=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    dostepny = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def __str__(self):
        return self.nazwa


class Zamowienie(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    data_zamowienia = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("nowe", "Nowe"),
            ("przyjęte", "Przyjęte"),
            ("wysłane", "Wysłane"),
            ("zrealizowane", "Zrealizowane"),
            ("anulowane", "Anulowane"),
        ],
        default="nowe",
    )

    class Meta:
        verbose_name = "Zamówienie"
        verbose_name_plural = "Zamówienia"

    def __str__(self):
        return f"Zamówienie {self.id} - {self.klient}"


class PozycjaZamowienia(models.Model):
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE, related_name="pozycje")
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    ilosc = models.PositiveIntegerField(default=1)
    cena_sztuka = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Pozycja zamówienia"
        verbose_name_plural = "Pozycje zamówień"

    def __str__(self):
        return f"{self.ilosc}x {self.produkt.nazwa} w zamówieniu {self.zamowienie.id}"
