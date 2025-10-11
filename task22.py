#todo: Модифицировать программу таким образом чтобы она выводила
# приветствие "Hello", которое только что записали в файл text.txt

# f = open("text.txt", "w+t")
# f.write("Hello\n")
# Ваше решение.

# f.close()

f = open("text1.txt", "w+t")
f.write("Hello\n")

with open("text1.txt", "r+t") as f:
    y = f.read()
print(y)

f.close()