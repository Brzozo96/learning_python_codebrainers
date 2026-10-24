def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b
    
def podziel(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        raise ValueError("Nie można dzielić przez zero!")
    except TypeError:
        raise ValueError("Niepoprawne typy danych!")
    finally:
        print("Wykonano operację dzielenia")