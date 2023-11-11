numbers = input("Введите числа, разделенные пробелами: ")
numbers_list = [int(x) for x in numbers.split()]

average = sum(numbers_list) / len(numbers_list)
print(f"Среднее арифметическое: {average}")

sorted_numbers = sorted(numbers_list)

sorted_tuple = tuple(sorted_numbers)
print("Отсортированный кортеж: ", sorted_tuple)
