import pytest
from kalkulator import dodaj

@pytest.mark.dodaj_z_parametrami
@pytest.mark.parametrize("num_1, num_2, expected_result", [
    (1, 1, 2),
    (2, 3, 5),
    (-1, 1, 0),
    (-1, -1, -2),
    (1.5, 2.5, 4.0),
    (0, 0, 0)
])
def test_dodaj_z_parametrami(num_1, num_2, expected_result):
    assert dodaj(num_1, num_2) == expected_result


