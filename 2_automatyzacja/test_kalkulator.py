import pytest
from kalkulator import dodaj, odejmij, pomnoz, podziel

@pytest.mark.dodaj
def test_dodaj():
    assert dodaj(1, 1) == 2
    assert dodaj(2, 3) == 5
    assert dodaj(-1, 1) == 0
    assert dodaj(-1, -1) == -2
    assert dodaj(1.5, 2.5) == 4.0
    assert dodaj(0, 0) == 0

@pytest.mark.odejmij
def test_odejmij():
    assert odejmij(1, 1) == 0
    assert odejmij(2, 3) == -1
    assert odejmij(-1, 1) == -2
    assert odejmij(-1, -1) == 0
    assert odejmij(1.5, 2.5) == -1.0
    assert odejmij(0, 0) == 0

@pytest.mark.pomnoz
def test_pomnoz():
    assert pomnoz(1, 1) == 1
    assert pomnoz(2, 3) == 6
    assert pomnoz(-1, 1) == -1
    assert pomnoz(-1, -1) == 1
    assert pomnoz(1.5, 2.5) == 3.75
    assert pomnoz(0, 0) == 0

@pytest.mark.podziel
def test_podziel():
    assert podziel(1, 1) == 1
    assert podziel(2, 3) == 2/3
    assert podziel(-1, 1) == -1
    assert podziel(-1, -1) == 1
    assert podziel(1.5, 2.5) == 0.6
    assert podziel(0, 0) == pytest.raises(ZeroDivisionError)

    