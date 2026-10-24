# a jest równe b: a == b
# a jest różny od b: a != b
# a jest większe od b: a > b
# a jest mniejsze od b: a < b
# a jest większe lub równe b: a >= b
# a jest mniejsze lub równe b: a <= b

nasz_wiek = 20
dopuszczalny_wiek = 18

print(nasz_wiek > dopuszczalny_wiek, '\n')

print('20 > 18: ', 20 > 18)
print('20 > 20: ', 20 > 20)
print('20 >= 20: ', 20 >= 20, '\n')

print('20 < 20: ', 20 < 20)
print('20 <= 20: ', 20 <= 20, '\n')

print('20 == 20: ', 20 == 20)
print('20 != 20: ', 20 != 20, '\n')

print("20 = '20': ", 20 == '20', '\n')