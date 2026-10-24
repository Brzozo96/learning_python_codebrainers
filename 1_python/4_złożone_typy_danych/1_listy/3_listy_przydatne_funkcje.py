lista_imion_1 = ["Czarek", "Darek", "Ela", "Artur", "Bartek"]
lista_imion_2 = ["Czarek", "Darek", "Ela", "Artur", "Bartek"]

"""
Metoda zwraca pierwszą listę posortowaną
Metoda sort() modyfikuje listę na miejscu
"""
wynik = sorted(lista_imion_1)
lista_imion_2.sort()

print("lista_imion_1", lista_imion_1)
print("lista imion 2 ", lista_imion_2)
print("Wynik ", wynik)
print()

"""
Enumerate zwraca indeks i wartość elementu z listy
"""

print("enumerate", list(enumerate("Artur")))
print("enumerate", list(enumerate(lista_imion_2)))
