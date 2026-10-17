"""
1. Listy imion - stworz liste z 3-ema imionami
2. dodaj pojedyncze imie do listy
3. stworz nowa liste z dwoma imionami i dodaj je
4. stworz nowa liste z dwoma imionami i dodaj je na poczatek listy
5. posortuj te liste
6. zwroc 4 elementy listy
"""

lista_imion = ["Ania", "Kasia", "Basia"]
lista_imion.append("Bartek")
print("2:", lista_imion, "\n")

nowe_imiona = ["Krzyś", "Ryś"]
lista_imion.extend(nowe_imiona)
print("3:", lista_imion, "\n")

nowe_imiona = ["Celina", "Malina"]
lista_imion = nowe_imiona + lista_imion
print("4:", lista_imion, "\n")

# lista_imion.sort() nadpisuje liste oryginalna
wynik = sorted(lista_imion)
print("5:", wynik, "\n")

print("6:", wynik[:4], "\n")


print("7:", wynik[:len(wynik)//2], "\n")