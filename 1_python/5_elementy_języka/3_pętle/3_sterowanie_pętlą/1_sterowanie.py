imiona = ["Artur", "Adam", "Ania", "Krzysiek", "Kasia", "Ola", "Jacek"]

for imie in imiona:
    is_woman = imie[-1] == "a"
    if is_woman:
        continue
    print(f"cześć {imie}")

for imie in imiona:
    is_woman = imie[-1] == "a"
    if is_woman:
        break
    print(f"cześć {imie}")
