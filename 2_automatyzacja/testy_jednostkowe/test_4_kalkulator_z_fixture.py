import pytest
from kalkulator import dodaj




@pytest.mark.dodaj_z_fixture
def test_dodaj(przygotowanie, oczekiwany_wynik_dodawania):
    assert dodaj(1, 2) == oczekiwany_wynik_dodawania

    
@pytest.mark.dodaj_z_fixture
def test_dodaj_2(przygotowanie):
    assert dodaj(1, 2) == 3

@pytest.mark.dodaj_z_fixture
def test_dodaj_3(przygotowanie):
    assert dodaj(1, 2) == 3
