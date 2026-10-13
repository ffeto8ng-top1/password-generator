import random
import string

def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    # Если ничего не выбрано — включаем всё по умолчанию
    if not (use_letters or use_digits or use_symbols):
        use_letters = use_digits = use_symbols = True

    chars = ""
    required_chars = []

    if use_letters:
        chars += string.ascii_letters
        required_chars.append(random.choice(string.ascii_letters))
    if use_digits:
        chars += string.digits
        required_chars.append(random.choice(string.digits))
    if use_symbols:
        # Можно поменять набор символов под себя
        symbols = "!@#$%^&*()-_=+[]{};:,."
        chars += symbols
        required_chars.append(random.choice(symbols))

    # Минимальная длина — столько типов символов мы решили использовать
    min_length = len(required_chars)
    if length < min_length:
        length = min_length

    # Добираем оставшиеся символы
    password_chars = required_chars + [random.choice(chars) for _ in range(length - min_length)]

    random.shuffle(password_chars)
    return ''.join(password_chars)

# Пример интерактивного использования
if __name__ == "__main__":
    try:
        length = int(input("Длина пароля (например, 12): "))
    except ValueError:
        print("Некорректная длина, ставим 12.")
        length = 12

    use_letters = input("Включить буквы? (да/нет): ").strip().lower() != "нет"
    use_digits = input("Включить цифры? (да/нет): ").strip().lower() != "нет"
    use_symbols = input("Включить спецсимволы? (да/нет): ").strip().lower() != "нет"

    password = generate_password(length, use_letters, use_digits, use_symbols)
    print("Твой пароль:", password)
