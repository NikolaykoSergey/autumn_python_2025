# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

# Пример использования
# user = User("test@example.com", "secret")
# print(user.email)  # test@example.com
# # print(user.password) # AttributeError
# print(user.check_password("secret"))  # True
# print(user.check_password("wrong"))   # False

class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self._password_hash = hash(password)

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if "@" not in value:
            raise ValueError("Некорректный email: отсутствует символ @")
        self._email = value

    def check_password(self, password: str) -> bool:
        return hash(password) == self._password_hash

# Пример использования
user = User("test@example.com", "secret")
print(user.email)
print(user.check_password("secret"))
print(user.check_password("wrong"))
