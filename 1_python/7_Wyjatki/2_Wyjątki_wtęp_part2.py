

liczba = 5
słowo = input("podaj mi liczbę do podzielenia ")

try:
    print("\nChce spróbować ten ryzykowny kod\n")
    wynik = liczba / słowo
    print(wynik)
    print("\nUdało się wykonać ryzykowny kod\n")

except ZeroDivisionError as błąd:
    print(f"\nWystąpił błąd dzielenia przez zero : {str(błąd).upper()}")

except TypeError as błąd:
    print(f"\nWystąpił błąd Typów : {str(błąd).upper()}")

except Exception as błąd:
    print(f"\nWystąpił nieznany błąd : {str(błąd).upper()}")


# print("\nchciałbym żeby to się wyświetliło zawsze.\n".upper())

