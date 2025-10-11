#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла inverted_sort.txt
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.

# Результат
#Complex is better than complicated.
#Simple is better than complex.
#Explicit is better than implicit.
#Beautiful is better than ugly.

f = open('inverted_sort.txt', "w+t", encoding = 'utf-8' )
f.write("""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
""")
f.write('\n')
f.close()

with open('inverted_sort.txt', 'r+') as f:
    line = f.readlines()
    lines = list(reversed(line))

    for line_ in lines:
        f.write(line_)
    f.close()
