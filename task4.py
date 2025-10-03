x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = int(input('Введите z: '))
if x >= y or x >= z:
    a = x
    if y >= z or y >= x:
        a = y
    else:
        a = z
print('Наибольшее число: ' + str(a))