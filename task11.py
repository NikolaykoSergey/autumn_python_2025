x :int = int(input('Введите число месяца: '))
if x == 0 or x > 12:
    print('Error')
    exit(100)
if 1 <= x <= 2 or x == 12:
    print('Зима')
elif 2 < x < 6:
    print('Весна')
elif 5 < x < 9:
    print('Лето')
elif x > 8 or x < 12:
    print('Осень')