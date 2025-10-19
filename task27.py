# todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

def numbers_to_letters():
    text = input("Введите строку: ")
    result = []

    for token in text.split():
        if token.isdigit():
            num = int(token)
            if 1 <= num <= 26:
                result.append(chr(num + 96))
            else:
                result.append(token)
        else:
            result.append(token)
    output = ''
    for t in result:
        if t.isalpha():
            output += t
        else:
            output += t
    print(f"""
    input                         output
    {text}                        
                                  {output}
    """)
numbers_to_letters()


