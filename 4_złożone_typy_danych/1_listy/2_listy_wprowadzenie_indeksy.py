imiona = ["Artur", "Bartek", "Czarek", "Darek", "Ela"]

print(imiona[1]) # string "Bartek"
print(imiona[1][-3]) # "t"

print(imiona[::2])

nowa_lista = imiona + imiona[::-1]
print(nowa_lista)

imiona[-1] = "Edward"
print(imiona)

# metody - funkcje wykonywane na obiekcie

# append(20)
imiona.append(20) # dodaje pojedyńczą rzecz
print("Dodanie elementu 20:", imiona)

imiona.extend([1, 2, 3]) # rozszerza o nową listę
print("Dodanie extend:", imiona)

