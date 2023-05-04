password = input("Ведите пароль: ")
score = 0

if len(password) >= 8:
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char in '+-/_%$#@;*&^:?><}{[]!' for char in password):
    score += 1

print(f"Количество балов за пароль: {score}")

if score == 0:
    print("Пароль слабый. Нужно использовать больше разных символов и длину пароля.")
elif score < 5:
    print("Пароль можно улучшить, используя больше символов и увеличивая его длину.")
else:
    print("Пароль сложный и надежный!")
