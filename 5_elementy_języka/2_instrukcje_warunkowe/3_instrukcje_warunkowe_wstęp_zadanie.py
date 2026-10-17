imie = "Artur"


imie[-1] == "a" # sprawdzenie czy żeńskie


imie = input("Podaj imię: ")

if imie[-1].lower() == "a":
    print("RÓŻOWY")
else:
    print("NIEBIESKI")
