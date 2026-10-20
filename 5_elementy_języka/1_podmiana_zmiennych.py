duza_liczba = 1
mala_liczba = 90000

print("\nPrzed zmianą")
print(f"Duża liczba {duza_liczba}")
print(f"Mała liczba {mala_liczba}")

mala_liczba, duza_liczba = duza_liczba, mala_liczba

print("\nPo zmianie")
print(f"Duza liczba: {duza_liczba}")
print(f"Mała liczba: {mala_liczba}")


imie_1, imie_2, *reszta_imion = ["Jacek", "Maciek", "Tomek", "Janek", "Kasia"]

print("\nImiona")
print(f"Imie 1: {imie_1}")
print(f"Imie 2: {imie_2}")
print(f"Reszta imion: {reszta_imion}")