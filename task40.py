# Система уведомлений (Полиморфизм)
# todo: Реализовать систему отправки уведомлений пользователям через разные каналы.
#
# Требования:
# Базовый класс NotificationSender с методом send(message, user)
# Дочерние классы:
# EmailSender: отправляет email с темой "Образовательная платформа"
# SMSSender: отправляет SMS (первые 50 символов сообщения)
# PushSender: отправляет push-уведомление с иконкой "🎓"
#
# Класс пользователя User:
# Свойства: name, preferred_notifications (список объектов NotificationSender)


# Этот код должен работать после релизации:
# user = User("Мария", [EmailSender(), PushSender()])
# notify_user(user, "Блок аналитики начинается с 27 октября!")
#
# def notify_user(user, message):
#     for sender in user.preferred_notifications:
#         sender.send(message, user)

class NotificationSender:
    def send(self, message, user):
        raise NotImplementedError("Метод должен быть переопределён в подклассе")


class EmailSender(NotificationSender):
    def send(self, message, user):
        print(f"📧 Отправлено письмо пользователю {user.name}:")
        print(f"Тема: Образовательная платформа")
        print(f"Сообщение: {message}\n")


class SMSSender(NotificationSender):
    def send(self, message, user):
        short_msg = message[:50]
        print(f"📱 Отправлено SMS пользователю {user.name}:")
        print(f"Текст: {short_msg}\n")


class PushSender(NotificationSender):
    def send(self, message, user):
        print(f"🎓 Push-уведомление для {user.name}: {message}\n")


class User:
    def __init__(self, name, preferred_notifications):
        self.name = name
        self.preferred_notifications = preferred_notifications


def notify_user(user, message):
    for sender in user.preferred_notifications:
        sender.send(message, user)


user = User("Мария", [EmailSender(), PushSender()])
notify_user(user, "Блок аналитики начинается с 27 октября!")
