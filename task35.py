# Инкапсуляция и property
# todo: Класс "Температура"
# Создайте класс Temperature, который хранит температуру в градусах Цельсия.
# Добавьте свойство для получения и установки температуры в Фаренгейтах и Кельвинах.
# Внутренне температура должна храниться только в Цельсиях.

# celsius (get, set) - работа с Цельсиями.
# fahrenheit (get, set) - при установке конвертирует значение в Цельсии.
# kelvin (get, set) - при установке конвертирует значение в Цельсии.

# Пример использования
# t = Temperature(25)
# print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
# t.fahrenheit = 32
# print(f"После установки 32F: {t.celsius}C")

class Temperature:
    def __init__(self, celsius: float = 0.0):
        self._celsius = celsius  # внутреннее хранение температуры в Цельсиях

    @property
    def celsius(self) -> float:
        """Возвращает температуру в Цельсиях."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        """Устанавливает температуру в Цельсиях."""
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Возвращает температуру в Фаренгейтах."""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        """Устанавливает температуру в Фаренгейтах и конвертирует в Цельсии."""
        self._celsius = (value - 32) * 5/9

    @property
    def kelvin(self) -> float:
        """Возвращает температуру в Кельвинах."""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float):
        """Устанавливает температуру в Кельвинах и конвертирует в Цельсии."""
        self._celsius = value - 273.15

    def __repr__(self):
        return f"Temperature(celsius={self._celsius})"

# Пример использования
temp = Temperature(25)  # создаём объект с температурой 25°C

print("Температура в Цельсиях:", temp.celsius)
print("Температура в Фаренгейтах:", temp.fahrenheit)
print("Температура в Кельвинах:", temp.kelvin)

temp.fahrenheit = 68    # устанавливаем температуру в Фаренгейтах
print("\nПосле установки 68°F:")
print("Температура в Цельсиях:", temp.celsius)

temp.kelvin = 300       # устанавливаем температуру в Кельвинах
print("\nПосле установки 300 K:")
print("Температура в Цельсиях:", temp.celsius)
