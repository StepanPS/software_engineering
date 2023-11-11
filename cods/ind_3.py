def big_number(sequence):
    numbers_counts = {}

    for digit in sequence:
        if digit.isdigit():
            digit = int(digit)
            numbers_counts[digit] = numbers_counts.get(digit, 0) + 1

    sorted_counts = sorted(numbers_counts.items(), key=lambda x: x[1], reverse=True)

    top = sorted_counts[:3]

    top_three = sorted(top, key=lambda x: x[0])

    return dict(top_three)


sequence = input("Введите цифры (минимум 15): ")

if len(sequence) < 15:
    print("Я же предупредил, минимум 15!")
else:
    result = big_number(sequence)
    print("Словарь из 3-х самых часто встречаемых чисел:", result)
