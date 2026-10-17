słownik_walut = {
    "PLN": "Polski Złoty",
    "EUR": "Euro",
    "USD": "Dolar Amerykański",
    "JPY": "Japoński Jen"
}

# print(słownik_walut["Yuan"])
# print(słownik_walut.get("Yuan", "nie ma takiej waluty"))
# print("nie wyświetli się jeśli był błąd")

# 1. stwórz listę wartości słownika
lista_walut = list(słownik_walut.values())
print(lista_walut, '\n')

# 2. posortuj listę wartości słownika
lista_walut.sort()
print(lista_walut)