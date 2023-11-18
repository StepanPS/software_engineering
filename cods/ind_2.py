def add_expense(file_name, amount, category):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f"Сумма: {amount}, причина: {category}\n")

def view_expenses(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        expenses = f.readlines()
        for expense in expenses:
            amount, category = expense.strip().split(',')
            print(f"{amount},  {category}")

file_name = "Расходы.txt"
while True:
    print("1. Добавить расходы")
    print("2. Просмотр текущих расходов")
    print("3. Выход")
    choice = input("Выберите одно из трёх: ")

    if choice == "1":
        amount = input("Введите сумму: ")
        category = input("Причина затраты: ")
        add_expense(file_name, amount, category)
    elif choice == "2":
        view_expenses(file_name)
    elif choice == "3":
        break
    else:
        print("Неверный выбор")
