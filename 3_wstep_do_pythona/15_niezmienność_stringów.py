imie = "python"

#imie[0] = "p" nie zadziała bo jest niedozwolone

imie = "P" + imie[1:] #ython

print(imie)

słowo = "Artur Babiński  "
print(len(słowo))


alfabet = "abcdefghijklmnopqrstuvwxyz" #26

dlugosc = len(alfabet)

print(alfabet[:(dlugosc//2)])

# num_1 = 6
# num_2 = 2
# wynik = num_1 / num_2  <- dzielenie zwraca typ float

# print(wynik) # 3
# print(int(wynik)) # 3

# wynik = num_1 // num_2
# print(wynik)


