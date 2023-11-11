main = input("Введите  числа: ")
List = [int(num) for num in main.split()]

Tuple = tuple(List)

print("Список чисел:", List)
print("Кортеж чисел:", Tuple)
