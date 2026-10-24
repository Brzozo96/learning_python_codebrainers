import pytest

@pytest.fixture
def przygotowanie():
    print("\n Start testu dodawania\n".upper())
    yield
    print("\n Koniec testu dodawania\n")
    
@pytest.fixture(scope="session", autouse=True)
# @pytest.fixture(scope="function", autouse=True)
def przygotowanie_autouse():
    print("\n Na poczatku sesji".upper())
    yield
    print("\n Koniec sesji".upper())


@pytest.fixture
def oczekiwany_wynik_dodawania():
    return 3
    

@pytest.fixture
def uzytkownik_premium():
    słownik = {
        "username": "tester_pro",
        "email": "tester@example.com",
        "is_premium": True,
        "punkty": 120
    }
    return słownik
