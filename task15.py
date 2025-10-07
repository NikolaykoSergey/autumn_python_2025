#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

mass = []
N = int(input('Введите длину массива: '))
for x in range(N):
    x = int(input('Введите элемент массива: '))
    mass.append(x)
print('Изначальный массив: ' + str(mass))
new_mass = []
for x in mass:
    x += 1
    new_mass.append(x)
print('Новый массив, где каждый элемент увеличен на 1: ' + str(new_mass))