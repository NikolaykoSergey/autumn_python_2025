 # todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.

# prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99",  "18.99", "N/A", "¥5000"]

prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99",  "18.99", "N/A", "¥5000"]

# Примерные курсы валют
exchange_rates = {
    "USD": 90,
    "EUR": 100,
    "JPY": 0.60,
}

def convert_to_rub(price_str):
    if "₽" in price_str:
        return float(price_str.replace("₽", ""))
    elif "USD" in price_str:
        return float(price_str.replace(" USD", "")) * exchange_rates["USD"]
    elif "€" in price_str:
        return float(price_str.replace("€", "")) * exchange_rates["EUR"]
    elif "$" in price_str:
        return float(price_str.replace("$", "")) * exchange_rates["USD"]
    elif "¥" in price_str:
        return float(price_str.replace("¥", "")) * exchange_rates["JPY"]
    else:
        try:
            return float(price_str)
        except ValueError:
            return None

ruble_prices = [convert_to_rub(price) for price in prices if convert_to_rub(price) is not None]
print(ruble_prices)