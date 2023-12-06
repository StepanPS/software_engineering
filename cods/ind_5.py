class CustomException(Exception):
    pass

try:
       number = int(input("Введите число: "))
    if number % 2 != 0:
        raise CustomException("Введено нечетное число!")
    else:
        print("Введено четное число.")
except CustomException as e:
    print(e)

try:
       name = input("Введите имя: ")
    if name == "":
        raise CustomException("Имя не может быть пустым!")
    else:
        print(f"Привет, {name}!")
except CustomException as e:
    print(e)
