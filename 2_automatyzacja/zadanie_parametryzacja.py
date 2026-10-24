import pytest

# stwórz testową która będzie parametryzowana
# funckja ma przyjmować imię i nazwisko i zwracać łączne powitanie np.
# "Witaj, Jan Kowalski" z uwzględniem że pełne imię ma być zwracane zawe z dużej litery

# @pytest.mark.powitanie
# @pytest.mark.parametrize("imie, nazwisko, spodziewany_rezultat", [
#     ("Jan", "kowalski", "Witaj, Jan Kowalski"),
#     ("jan", "kowalski", "Witaj, Jan Kowalski"),
#     ("Jan", "Kowalski", "Witaj, Jan Kowalski"),
#     ("jan", "kowalski", "Witaj, Jan Kowalski"),
# ])

# def test_powitanie(imie, nazwisko, spodziewany_rezultat):
#     assert powitanie(imie, nazwisko) == spodziewany_rezultat


def powitanie(imie: str, nazwisko: str):
    powitanie = f"Witaj, {imie.capitalize()} {nazwisko.capitalize()}"
    return powitanie


@pytest.mark.powitanie
@pytest.mark.parametrize("imie, nazwisko, spodziewany_rezultat", [
    ("Jan", "kowalski", "Witaj, Jan Kowalski"),
    ("jan", "kowalski", "Witaj, Jan Kowalski"),
    ("Jan", "Kowalski", "Witaj, Jan Kowalski"),
    ("jan", "kowalski", "Witaj, Jan Kowalski")
])
def test_powitanie(imie, nazwisko, spodziewany_rezultat):
    assert powitanie(imie, nazwisko) == spodziewany_rezultat

# # stwórz testową która będzie parametryzowana
# # funckja ma przyjmować imię i nazwisko i zwracać łączne powitanie np.
# # "Witaj, Jan Kowalski" z uwzględniem że pełne imię ma być zwracane zawe z dużej litery

# @pytest.mark.powitanie
# @pytest.mark.parametrize("imie, nazwisko, oczekiwany_wynik", [
#     ("Jan", "kowalski", "Witaj, Jan Kowalski"),
#     ("jan", "kowalski", "Witaj, Jan Kowalski"),
#     ("Jan", "Kowalski", "Witaj, Jan Kowalski"),
#     ("jan", "kowalski", "Witaj, Jan Kowalski"),
# ])

# def test_powitanie(imie, nazwisko, oczekiwany_wynik):
#     assert f"Witaj, {imie.capitalize()} {nazwisko.capitalize()}" == oczekiwany_wynik
