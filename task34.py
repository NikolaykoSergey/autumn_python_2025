from db import DEFENITION_WORD   # убедись, что словарь лежит в db/txt.py
import random
import uuid
import datetime
import os


# ==== Класс управления сохранениями ====
class SaveGame:
    FILE_NAME = "save_game.csv"

    def save(self, id_session, name, word, mask):
        """💾 Сохраняет игру"""
        with open(self.FILE_NAME, "at", encoding="utf-8") as f:
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            mask_str = "".join(mask)
            line = f"{dt}|{id_session}|{name}|{word}|{mask_str}\n"
            f.write(line)
        print("💾 Игра сохранена!")

    def load(self, name):
        """📂 Загружает игру по имени"""
        if not os.path.exists(self.FILE_NAME):
            print("❌ Нет сохранённых игр!")
            return None

        with open(self.FILE_NAME, "r", encoding="utf-8") as f:
            list_str = f.readlines()

        found = [i for i, s in enumerate(list_str) if name in s]
        if not found:
            print("❌ Сохранений для этого имени нет!")
            return None

        print("📂 Ваши сохранения:")
        for i, idx in enumerate(found):
            print(i, ")", list_str[idx].strip())

        try:
            indx_load = int(input("Введите номер сохранения: "))
            sg = list_str[found[indx_load]].split("|")
            session_uuid = sg[1]
            key = sg[3].strip()
            mask = list(sg[4].strip())
            print("✅ Игра загружена!")
            return session_uuid, key, mask
        except (IndexError, ValueError):
            print("❌ Ошибка при выборе сохранения!")
            return None


# ==== Основной класс игры ====
class YaKube:
    def __init__(self):
        self.name = input("Введите имя: ")
        self.save_manager = SaveGame()

    # ==== Меню ====
    def print_menu(self):
        print("""   
       📋 Меню:
       1️⃣  Начать игру
       2️⃣  Сохранить игру
       3️⃣  Загрузить игру
       4️⃣  Выход из игры
        """)

    # ==== Генерация случайного слова ====
    def generate_key(self) -> str:
        keys = list(DEFENITION_WORD.keys())
        random.shuffle(keys)
        return keys.pop()

    # ==== Основная логика игры ====
    def start_game(self, session_uuid, key, mask, list_word):
        print(f"📘 Подсказка: {DEFENITION_WORD[key]}")
        print("Текущее слово:", "".join(mask))

        while '#' in mask:
            alfa = input("Введите букву (или '2' — сохранить, '4' — выход): ").lower()

            if alfa == "2":
                self.save_manager.save(session_uuid, self.name, key, mask)
                continue
            elif alfa == "4":
                print(f"👋 Спасибо, {self.name}, за игру!")
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

        print(f"🎉 Поздравляем, {self.name}! Вы отгадали слово: {key}")

    # ==== Запуск новой игры ====
    def new_game(self):
        key = self.generate_key()
        list_word = list(key)
        mask = ['#'] * len(key)
        session_uuid = uuid.uuid4()
        self.start_game(session_uuid, key, mask, list_word)

    # ==== Загрузка сохранения ====
    def load_game(self):
        result = self.save_manager.load(self.name)
        if result:
            session_uuid, key, mask = result
            self.start_game(session_uuid, key, mask, list(key))

    # ==== Главный цикл меню ====
    def run(self):
        while True:
            self.print_menu()
            try:
                num = int(input("Выберите пункт меню: "))
            except ValueError:
                print("❌ Введите число от 1 до 4.")
                continue

            match num:
                case 1:
                    self.new_game()
                case 2:
                    print("💾 Сохранить можно только во время игры (введите '2').")
                case 3:
                    self.load_game()
                case 4:
                    print(f"👋 Пока, {self.name}! До встречи!")
                    break
                case _:
                    print("❌ Неверный пункт меню. Попробуйте снова.")


# ==== Точка входа ====
if __name__ == "__main__":
    game = YaKube()
    game.run()