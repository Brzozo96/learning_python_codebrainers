
liczba = 1
try:
    wynik = 10 / liczba

except ZeroDivisionError:
    print(f"Wystąpił błąd ZeroDivisionError")

except TypeError:
    print(f"Wystąpił błąd TypeError")

except Exception:
    print(f"Wystąpił błąd")

else:
    print(f"Try wykonał się poprawnie, a wynik to {wynik}")

finally:
    print("finally : Wykonam się zawsze na końcu bo jestem \"finally\" ")

