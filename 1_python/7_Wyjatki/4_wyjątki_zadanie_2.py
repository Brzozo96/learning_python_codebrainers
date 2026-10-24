# 1. Przyjmij od użytkownika dwie liczby, które chciałby ze sobą podzielić.
# 2. Zabezpiecz ten program na wypadek różnych nieprzewidzianych zdarzeń.




while True:
    try:
        input_1 = input("Podaj pierwszą liczbę: ")
        input_1 = float(input_1)
        break

    except ValueError:
        print(f"Wpisz typu 1, 2, etc. Została wpisana błędna wartość {input_1}")

    except Exception:
        print(f"Niespodziewany błąd. ")


while True:
    try:
        input_2 = input("Podaj drugą liczbę: ")
        input_2 = float(input_2)
        if input_2 == 0.0:
            raise ZeroDivisionError
        break

    except ZeroDivisionError:
        print(f"Podana liczba nie może być = 0")

    except ValueError:
        print(f"Wpisz typu 1, 2, etc. Została wpisana błędna wartość {input_2}")

    except Exception:
        print(f"Niespodziewany błąd. ")
