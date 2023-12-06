def sum_with_user_input():
    try:
        num = float(input("Введите число: "))
        result = int(2 + num)
        print(f"Результат: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")


if __name__ == '__main__':
    sum_with_user_input()
