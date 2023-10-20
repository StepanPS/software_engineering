number = int(input("Введите число от 0 до 10: "))
if 0 <= number <= 10:
    if number <= 3:
        print(f"Число {number} находится между 0 и 3")
    elif number < 6:
        print(f"Число {number} находится между 3 и 6")
    else:
        print(f"Число {number} находиться между 6 и 10")
