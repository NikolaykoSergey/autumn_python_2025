#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.

#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................


vol = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'

vol_ = {}
with open('messenge.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for x in text:
    if x in vol:
        x_ = x.lower()
        vol_[x_] = vol_.get(x_, 0) + 1

for vol, x_ in sorted(vol_.items()):
    print(f"Количество букв {vol} - {x_}")