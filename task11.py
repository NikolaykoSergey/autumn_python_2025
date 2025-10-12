#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название соответствующего
#  времени года ("зима", "весна" и т.д.).


x :int = int(input('Введите число месяца: '))
if x == 0 or x > 12:
    print('Error')
    exit(100)
def times():
    if 1 <= x <= 2 or x == 12:
        return ('Зима')
    elif 2 < x < 6:
        return ('Весна')
    elif 5 < x < 9:
        return ('Лето')
    else:
        return ('Осень')
rez = times()
print(f"время года: {rez}")