# todo: Исправить ошибку в коде игры  ../code/ya_kube.py

#from lesson_5.code import ya_kube



from db import DEFENITION_WORD   # убедись, что словарь лежит в db/txt.py

import random
import uuid
import datetime
import os



# ==== Ввод имени ====
name = input("Введите имя: ")


# ==== Меню ====
def print_menu():
    print("""   
       📋 Меню:
       1️⃣  Начать игру
       2️⃣  Сохранить игру
       3️⃣  Загрузить игру
       4️⃣  Выход из игры
    """)


# ==== Генерация случайного слова ====
def generate_key() -> str:
    keys = list(DEFENITION_WORD.keys())
    random.shuffle(keys)
    return keys.pop()


# ==== Сохранение игры (как раньше) ====
def save_game(id_session, word, mask):
    with open("save_game.csv", "at", encoding="utf-8") as f:
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mask_str = "".join(mask)
        line = f"{dt}|{id_session}|{name}|{word}|{mask_str}\n"
        f.write(line)
    print("💾 Игра сохранена!")


# ==== Загрузка сохранения ====
def load_game():
    if not os.path.exists("save_game.csv"):
        print("❌ Нет сохранённых игр!")
        return

    with open("save_game.csv", "r", encoding="utf-8") as f:
        list_str = f.readlines()

    found = [i for i, s in enumerate(list_str) if name in s]
    if not found:
        print("❌ Сохранений для этого имени нет!")
        return

    print("📂 Ваши сохранения:")
    for i in found:
        print(i, ")", list_str[i].strip())

    try:
        indx_load = int(input("Введите номер сохранения: "))
        sg = list_str[indx_load].split("|")
        session_uuid = sg[1]
        key = sg[3].strip()
        mask = list(sg[4].strip())
        print("✅ Игра загружена!")
        start_game(session_uuid, key, mask, list(key))
    except (IndexError, ValueError):
        print("❌ Ошибка при выборе сохранения!")


# ==== Основная логика игры ====
def start_game(session_uuid, key, mask, list_word):
    print(f"📘 Подсказка: {DEFENITION_WORD[key]}")
    print("Текущее слово:", "".join(mask))

    while '#' in mask:
        alfa = input("Введите букву (или '2' — сохранить, '4' — выход): ").lower()

        if alfa == "2":
            save_game(session_uuid, key, mask)
            continue
        elif alfa == "4":
            print(f"👋 Спасибо, {name}, за игру!")
            return

        found = False
        for idx, char in enumerate(list_word):
            if alfa == char:
                mask[idx] = alfa
                found = True

        if found:
            print("✅ Есть такая буква!")
        else:
            print("❌ Нет такой буквы!")

        print("Текущее слово:", "".join(mask))

    print(f"🎉 Поздравляем, {name}! Вы отгадали слово: {key}")


# ==== Главный цикл меню ====
while True:
    print_menu()
    try:
        num = int(input("Выберите пункт меню: "))
    except ValueError:
        print("❌ Введите число от 1 до 4.")
        continue

    match num:
        case 1:
            key = generate_key()
            list_word = list(key)
            mask = ['#'] * len(key)
            session_uuid = uuid.uuid4()
            start_game(session_uuid, key, mask, list_word)

        case 2:
            print("💾 Сохранить можно только во время игры (введите '2').")

        case 3:
            load_game()

        case 4:
            print(f"👋 Пока, {name}! До встречи!")
            break

        case _:
            print("❌ Неверный пункт меню. Попробуйте снова.")
