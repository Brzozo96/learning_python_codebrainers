imiona = ["Artur", "Basia", "Celina", "Dawid", "Eliza"]


# for imie in imiona:
#     is_woman = imie[-1] == "a"
#     if is_woman:
#         print(f"Dzień dobry, Pani {imie}")
#     else:
#         print(f"Dzień dobry, Panie {imie}")


# for element in list(enumerate(imiona)):
#     print(f"Zawodnik {element[1]}, zajął miejsce {element[0] + 1}")

# x = (0, "Artur")
# print(x[0])
# print(x[1])

# zajęte_miejsce, imie = (0, "Artur")
# print(zajęte_miejsce)
# print(imie)


for zajęte_miejsce, imie in enumerate(imiona):
    print(f"Zawodnik {imie} zajął miejsce {zajęte_miejsce + 1}")

