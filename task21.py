#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.

# Содержимое файла config_default.txt
# Конфигурация приложения.
# app_name    = ?
# version     = ?
# debug       = ?

# Настройки базы данных
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?

# Настройки API
# api_key     = ?
# api_secret  = ?
# base_url    = ?

# Пути
# log_file    = ?
# data_dir    = ?
# temp_dir    = ?


# Данные для подстановки
# config_values = {
#     'app_name': 'NextGen',
#     'version': '1.0.0',
#     'debug':  True,
#     'db_host': 'localhost',
#     'db_port': 5432,
#     'db_name': 'my_database',
#     'db_user': 'admin',
#     'db_password': 'secret123',
#     'api_key': 'ak_123456789',
#     'api_secret': 'sk_987654321',
#     'base_url': 'https://api.example.com',
#     'log_file': '/var/log/app.log',
#     'data_dir': '/opt/app/data',
#     'temp_dir': '/tmp/app',
#     'max_workers': 10,
#     'timeout': 30,
#     'retry_attempts': 3
# }

	# В итоге вместо "?" должны подставиться значения и получиться файл config.txt:

# Конфигурация приложения
# app_name    =  "NextGen"
# version     =  '1.0.0'
# debug       =  True
#
# Настройки базы данных
#

f = open('config_default.txt', "w+t", encoding = 'utf-8' )
f.write("""
# Конфигурация приложения.
app_name    = ?
version     = ?
debug       = ?

# Настройки базы данных
db_host     = ?
db_port     = ?
db_name     = ?
db_user     = ?
db_password = ?

# Настройки API
api_key     = ?
api_secret  = ?
base_url    = ?

# Пути
log_file    = ?
data_dir    = ?
temp_dir    = ?
""")
f.close()

config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}
from string import Template
with open('config_default.txt', 'r+', encoding = 'utf-8') as f:
    config_text = f.read()
    f.close()
result = config_text
for value in config_values.values():
    result = result.replace("?", str(value), 1)
with open('config.txt', 'w', encoding = 'utf-8') as f:
    f.write(result)
    f.close()

