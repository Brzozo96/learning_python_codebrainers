zbiór = {"Artur", "Bartek", "Czarek"}

print(zbiór)

zbiór.add("Damian")
print("Po dodaniu Damiana:", zbiór, '\n')

zbiór.add("Damian")
zbiór.add("Damian")
zbiór.add("Damian")
print("Po dodaniu 3x Damiana:", zbiór, '\n')


lista = ["Artur", "Bartek", "Czarek", "Damian", "Damian", "Damian"]
print("lista:", lista, '\n')

lista_bez_powtórzeń = list(set(lista))
print("lista bez powtórzeń:", lista_bez_powtórzeń, '\n', f"o typie: {type(lista_bez_powtórzeń)}\n")

