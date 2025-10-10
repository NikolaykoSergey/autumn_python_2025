# todo: База данных пользователя.
# Задан массив объектов пользователя
from re import match

#users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#         {'login': 'Ivan',  'age': 10, 'group': "guest"},
#         {'login': 'Dasha', 'age': 30, 'group': "master"},
#         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

#Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
#,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
#1. По возрасту
#2. По первой букве
#3. По группе

#тип сортировки: 1

#Затем сообщение для ввода
#Ввидите критерии поиска: 16

#Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]
#print(users)
#for user in users:
#    if user['group'] == "guest":
#        print('Пользователь: ' + user['login'], 'Возраст: ' + str(user['age']) + ' лет', 'Группа: ' + user['group'])

def print_menu():
    print("""   
        1. По возрасту
        2. По первой букве
        3. По группе
    """)

print_menu()
num = int(input("Выберите тип сортировки из пунктов меню:"))

users_dict = {u['login']: u for u in users}

match num:
    case 1:
        x = int(input('Введите возраст: '))
        for user in users:
            if x < user['age']:
                print('Пользователь: ' + user['login'] + ',',
                      'Возраст: ' + str(user['age']) + ' лет' + ',',
                      'Группа: ' + user['group'])
            else:
                print('введено некорректное значение')
    case 2:
        sorted_users_dict = dict(sorted(users_dict.items(), key=lambda item: item[0]))

        for login, info in sorted_users_dict.items():
            print('Пользователь: ' + login + ',',
                  'Возраст: ' + str(info['age']) + ' лет,',
                  'Группа: ' + info['group'])
    case 3:
        sorted_items = sorted(users_dict.items(), key=lambda item: item[1]['group'])
        sorted_by_group = dict(sorted_items)
        for login, info in sorted_by_group.items():
            print(f"{info['group']}: {login}, возраст = {info['age']}")

        print("""
        Группы:   
        1. Admin
        2. Master
        3. Guest
    """)

        sort_group = int(input('Выберете группу: '))
        if sort_group == 1:
            x = {login: info for login, info in users_dict.items() if info.get('group') == 'admin'}
            for login, info in x.items():
                print(f"Группа: {info['group']}, пользователь: {info['login']}, возраст: {info['age']}")
        elif sort_group == 2:
            x = {login: info for login, info in users_dict.items() if info.get('group') == 'master'}
            for login, info in x.items():
                print(f"Группа: {info['group']}, пользователь: {info['login']}, возраст: {info['age']}")
        elif sort_group == 3:
            x = {login: info for login, info in users_dict.items() if info.get('group') == 'guest'}
            for login, info in x.items():
                print(f"Группа: {info['group']}, пользователь: {info['login']}, возраст: {info['age']}")
        else:
            print('Ввели несуществующую группу')




