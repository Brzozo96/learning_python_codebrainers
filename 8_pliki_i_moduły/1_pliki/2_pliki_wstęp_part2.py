nazwa_pliku = "dane_testowe_2.txt"

poziom_uprawnień = "a" # "r"- read "a"- append, "w"- write

file = open(nazwa_pliku, poziom_uprawnień, encoding="utf8")
file.write("\ncoś")

file.close()