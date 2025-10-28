# Модель учебных материалов
# todo: Создайте иерархию классов для представления различных типов учебных материалов.
#
# Требования: Базовый класс LearningMaterial:
# Свойства: title, author, duration_minutes
# Методы:
# display_info() - выводит основную информацию
# get_difficulty() - возвращает сложность материала (должен быть переопределен в дочерних классах)
#
# Дочерние классы:
# VideoLesson:
# Дополнительные свойства: video_quality, subtitles_available
# Сложность: "Средняя"
#
# Article:
# Дополнительные свойства: word_count, reading_level
# Сложность: рассчитывается как word_count / 1000 (легкая если <1, средняя 1-3, сложная >3)
#
# Quiz:
# Дополнительные свойства: questions_count, passing_score
# Сложность: "Высокая" если passing_score > 80, иначе "Средняя"


# Этот код должен работать после реализации:
# materials = [
#     VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True),
#     Article("Глубокое обучение", "Анна Петрова", 1200, "advanced"),
#     Quiz("Проверка знаний", "Платформа", 20, 75, 10)
# ]
#
# for material in materials:
#     print(f"{material.title}: {material.get_difficulty()}")

class LearningMaterial:
    def __init__(self, title, author, duration_minutes):
        self.title = title
        self.author = author
        self.uration_minutes = duration_minutes

    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Длительность: {self.duration_minutes} минут")

    def get_difficulty(self):
        raise NotImplementedError("Метод должен быть переопределён в подклассе")

class VideoLesson(LearningMaterial):
    def __init__(self, title, author, duration_minutes, video_quality, subtitles_available):
        super().__init__(title, author, duration_minutes)
        self.video_quality = video_quality
        self.subtitles_available = subtitles_available

    def get_difficulty(self):
        return "Средняя"


class Article(LearningMaterial):
    def __init__(self, title, author, word_count, reading_level):
        super().__init__(title, author, duration_minutes=0)  # длительность не указана
        self.word_count = word_count
        self.reading_level = reading_level

    def get_difficulty(self):
        ratio = self.word_count / 1000
        if ratio < 1:
            return "Легкая"
        elif 1 <= ratio <= 3:
            return "Средняя"
        else:
            return "Сложная"

class Quiz(LearningMaterial):
    def __init__(self, title, author, duration_minutes, passing_score, questions_count):
        super().__init__(title, author, duration_minutes)
        self.passing_score = passing_score
        self.questions_count = questions_count

    def get_difficulty(self):
        if self.passing_score > 80:
            return "Высокая"
        else:
            return "Средняя"


# Тестирование
materials = [
    VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True),
    Article("Глубокое обучение", "Анна Петрова", 1200, "advanced"),
    Quiz("Проверка знаний", "Платформа", 20, 75, 10)
]

for material in materials:
    print(f"{material.title}: {material.get_difficulty()}")


