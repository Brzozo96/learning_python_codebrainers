nazwa_pliku = "dane_testowe.txt"

poziom_uprawnień = "r" # "a", "w"

file = open(nazwa_pliku, poziom_uprawnień, encoding="utf8")


# pełen_teks = file.read() 
# print(pełen_teks, "\n")

pierwsza_linia = file.readline()
print(f"pIerwsza linia to: {pierwsza_linia}")

# druga_linia = file.readline()
# print(f"druga linia to: {druga_linia}")

wszystkie_pozostałe = file.readlines()
# print(f"wszystkie pozostałe to: {wszystkie_pozostałe}", "\n")


for linia in wszystkie_pozostałe:
    print(linia)

file.close()