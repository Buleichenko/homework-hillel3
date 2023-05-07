# Задание 1
text = input("Введите слово: ")

if text == text[::-1]:
    print("+")
else:
    print("-")

# Задание 2
text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

if word in text:
    print("YES")
else:
    print("NO")

# Задание 3
string = input("Введите строку: ")

if string.startswith('abc'):
    string = string.replace('abc', 'www', 1)
else:
    string += 'qqq'

print(string)

# Задание 4
text = input("Ведите текст с цифрами: ")

text_without_digits = ""
for char in text:
    if not char.isdigit():
        text_without_digits += char

print("Текст без цифр: ", text_without_digits)
# Задание 5
email = input("Введите электронную почту: ")

if "@" in email and "." in email:
    print("YES")
else:
    print("NO")
