day = int(input("Дата рождения: "))
month = int(input("Месяц рождения: "))
sign = ""

if (month == 2) and (day < 1 or day > 29):
    print("Ошибка: в феврале только 28 дней")
    exit()
if (month == 4 or month == 9 or month == 11) and (day < 1 or day > 30):
    print("Ошибка : в этом месяце 30 дней")
    exit()
if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day < 1 or day > 31):
    print("Ошибка : в этом месяце 31 день")
    exit()

if (month == 3 and day >= 21) or (month == 4 and day <= 20):
    sign = "Овен"
elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
    sign = "Телец"
elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
    sign = "Близнецы"
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    sign = "Рак"
elif (month == 7 and day >= 23) or (month == 8 and day <= 21):
    sign = "Лев"
elif (month == 8 and day >= 22) or (month == 9 and day <= 23):
    sign = "Дева"
elif (month == 9 and day >= 24) or (month == 10 and day <= 23):
    sign = "Весы"
elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
    sign = "Скорпион"
elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
    sign = "Стрелец"
elif (month == 12 and day >= 22) or (month == 1 and day <= 20):
    sign = "Козерог"
elif (month == 1 and day >= 21) or (month == 2 and day <= 18):
    sign = "Водолей"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    sign = "Рыбы"

if sign == "Овен":
    print("Овну выгодно показать себя перед начальством.")
elif sign == "Телец":
    print("Телец рискует оказаться против своей воли.")
elif sign == "Близнецы":
    print("Близнецы способны закружить водоворот общения и эмоций.")
elif sign == "Рак":
    print("Рак рискует столкнуться с такими не самыми лучшими проявлениями чувств, как жадность или зависть.")
elif sign == "Лев":
    print("Практически в любых делах Львом будет двигать здоровый азарт.")
elif sign == "Дева":
    print("События дня вполне способны поставить Деву в тупик.")
elif sign == "Весы":
    print("День склоняет Весы попробовать что-то новое.")
elif sign == "Скорпион":
    print("У Скорпиона могут быть большие проблемы.")
elif sign == "Стрелец":
    print("Звезды гороскопа целиком и полностью на стороне Стрельца.")
elif sign == "Козерог":
    print("Козерогу самое лучшее – попотеть на беговой дорожке или сходить в бассейн.")
elif sign == "Водолей":
    print("Водолею просто поверьте на слово: со стороны им виднее.")
elif sign == "Рыбы":
    print("Рыбы могут придавать каким-то событиям больше значения.")
else:
    print("Некорректный месяц рождения")
    exit()