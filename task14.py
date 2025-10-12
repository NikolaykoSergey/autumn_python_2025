#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
#
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.


mass = [1,2,17,54,30,89,2,1,6,2]
positions = {}

for i, val in enumerate(mass):
    if val not in positions:
        positions[val] = []
    positions[val].append(i)

for val, idxs in positions.items():
    if len(idxs) < 2:
        print(f"Для числа {val} нет минимального расстояния, т.к. элемент в массиве один.")
    else:
        min_dist = float('inf')
        pair = None
        for i in range(len(idxs) - 1):
            dist = idxs[i + 1] - idxs[i]
            if dist < min_dist:
                min_dist = dist
                pair = (idxs[i], idxs[i + 1])
        print(f"Для числа {val} минимальное расстояние в массиве по индексам: {pair[0]} и {pair[1]}")



