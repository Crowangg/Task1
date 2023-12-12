import os


def main():
    # Чтение значения из переменной окружения
    input_integer = os.getenv("MY_INTEGER_ENV")

    # Проверка, что значение не пустое
    if input_integer is None:
        print("Error: MY_INTEGER_ENV is not set.")
        return

    try:
        # Преобразование в целое число
        input_integer = int(input_integer)

        # Вывод в восьмеричной и шестнадцатеричной системах исчисления
        print(f"Decimal: {input_integer}")
        print(f"Octal: {oct(input_integer)}")
        print(f"Hexadecimal: {hex(input_integer)}")

    except ValueError:
        print("Error: Input is not a valid integer.")


if __name__ == "__main__":
    main()
