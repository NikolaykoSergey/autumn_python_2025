import ast  # todo: Определить в коде переменные:
# 1. Целочисленного типа
# 2. Вещественного типа
# 3. Логического типа
# 4. Строкового типа
# 5. Пустого типа
# Вывести их типы (надо погуглить).



# Определение типа объекта
# rez = ast.literal_eval(input('Введите переменную: '))
# if isinstance(rez, int):
#     print(str(rez) + ' - переменная целчисленного типа')
# elif isinstance(rez, str):
#     print(str(rez) + ' - переменная строкового типа')
# elif isinstance(rez, float):
#     print(str(rez) + ' - переменная вещественного типа')
# elif isinstance(rez, bool):
#     print(str(rez) + ' - переменная логического типа')
# elif isinstance(rez, None):
#     print(str(rez) + ' - пустая переменная')
# else:
#     print(str(rez) + ' - другой тип переменной')

rez = input('Введите переменную: ')
def type_class(rez):

    if rez == "None":
        return "None - пустая переменная"
    if rez.lower() in ["true", "false"]:
        return "bool - логический тип"
    if rez.lstrip('-').isdigit():
        return "int - целое число"
    if rez.count('.') == 1 and rez.replace('.', '').lstrip('-').isdigit():
        return "float - вещественное число"
    if (rez.startswith('"') and rez.endswith('"')) or (rez.startswith("'") and rez.endswith("'")):
        return "str - строка"

    return "Неизвестный тип"

rez_ = type_class(rez)
print(f"Определенный тип: {rez_}")