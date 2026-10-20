# 1. stwórz 2 zmienne - imie i wiek
# 2. stwórz warunek że jeżeli imię jest męskie i wiek jset >= 18 to wypisz "możesz iść na pobór do wojska"
# 3. jeżeli imię jest żeńskie i wiek jest >= 18 to wypisz "kobieta dorosła"
# 4. jeżeli wiek jest < 18 to wypisz "niepełnoletni"

imie = "Adam"
wiek = 30

is_male = imie[-1].lower() != 'a'
is_adult = wiek >= 18

if is_male and is_adult:
    print("Możesz iść na pobór do wojska")
elif not is_male and is_adult:
    print("Kobieta dorosła")
elif not is_adult:
    print("Jesteś nieletni")
else:
    print("poza zakresem")



if not is_adult:
    print("Jesteś nieletni")
elif not is_male:
    print("Kobieta dorosła")
else:
    print("Możesz iść na pobór do wojska")