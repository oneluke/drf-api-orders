# Łukasz Kacprzak - POD - projekt na zaliczenie Django REST API - System Zamówień

## Opis
Jest to aplikacja do zarządzania zamówieniami klientów.  
Obsługuje CRUD dla klientów, produktów, zamówień i pozycji zamówień.  
Zawiera zabezpieczenia oraz niestandardowe endpointy.

## Funkcjonalności
CRUD dla:
- Klientów (`/api/klienci/`)
- Produktów (`/api/produkty/`)
- Zamówień (`/api/zamowienia/`)
- Pozycji zamówień (`/api/pozycje/`)

Niestandardowe endpointy:
- **Zestawienie miesięczne zamówień** `/api/zestawienie-miesieczne/`
- **Lista zamówień dla klienta** `/api/zamowienia-klienta/<id>/`

Autoryzacja:
- **Tylko zalogowani użytkownicy mogą dodawać/edytować zamówienia**  
- **Odczyt dostępny dla wszystkich**  
- **Logowanie przez `/api-auth/login/`**