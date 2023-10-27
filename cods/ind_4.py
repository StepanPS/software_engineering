def main():
    values = []

    Inp = input("Введите числа через пробел: ")
    values =[float(val) for val in Inp.split()]

    if len(values) == 0:
        return 0
    else:
        return sum(values) / len(values)


if __name__ == "__main__":
    average = main()
    print("Среднее арифметическое:", average)
