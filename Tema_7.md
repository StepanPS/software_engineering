# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил:
- Пичкуренко Степан Сергеевич
- АИС-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | Не было |
| Задание 7 | + | Не было |
| Задание 8 | + | Не было |
| Задание 9 | + | Не было |
| Задание 10 | + | Не было |

Работу проверили:
- к.э.н., доцент Панов М.А.
## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_1.png )
## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку извашего файла, при этом используйте конструкцию open()/close().

```python
f = open('Text.txt', 'r',)
print(f.readline())
f.close()
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_2.png )
## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла массиве, при этом используйте конструкцию open()/close().

```python
f = open('Text.txt', 'r')
print(f.readlines())
f.close()
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_3.png)
## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('Text.txt') as f:
    print(f.readlines())
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_4.png )
## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('Text.txt') as f:
    for line in f:
        print(line)
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_5.png)
## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('Text.txt', 'a+') as f:
    f.write('\nMiraculously, the bear got out of the car and thought: “Miracles don’t happen!” - and climbed back.')

with open('Text.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_6_1.png )
### Как изменился файл Text.txt
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_6_2.png )

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
linse = ['one', 'two', 'three']
with open('Text.txt', 'w') as f:
    for line in linse:
        f.write('\nCycle run ' + line)
    print('Done!')
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_7_1.png )
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_7_2.png )

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
```python
import os


def print_docs(directory: str) -> None:
    global catalog
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)


if __name__ == '__main__':
    print_docs('/Users/Serega/Desktop/НИБ')
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_8.png )
## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст:
Приветствие
Спасибо
Извините
Пожалуйста
До свидания
Ты готов?
Как дела?
С днем рождения!
Удача!
Я тебя люблю.
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных

```python
def longest_words(file):
    with open(file, encoding='utf=8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

            if len(sought_words) == 1:
                return sought_words[0]
            return sought_words


print(longest_words('Text.txt'))
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_9.png )
## Лабораторная работа №10
### Требуется создать csv-файл «rows 300.csv» со следующими столбцами:
•	№ - номер по порядку (от 1 до 300);
•	Секунда - текущая секунда на вашем ПК;
•	Микросекунда - текущая миллисекунда на часах.
### Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/lab_10.png )

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
import re


def count_words(filename: str) -> tuple[int, str]:
    with open(filename, 'r', encoding='utf-8') as file:
        words: list[str] = [i for i in [re.sub("[-!.:«»,?""]", '', w.lower()) for w in file.read().split()] if
                            not i == ""]
        words_count: int = len(words)
        d: tuple[str, int] = sorted([(i, words.count(i)) for i in set(words)], key=lambda t: t[1], reverse=True)[0]
        return words_count, d[0]


count, word = count_words("Book.txt")
print(f"Кол-во слов: {count}\n Самое частое слово:'{word}'")
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/ind_1.png)
### Файл Book.txt.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/ind_1_1.png )

## Выводы
Код выводит два сообщения с найденными значениями: “Кол-во слов в файле” и “Самое частое слово”. Каждая строчка кода получилась индивидуальной:
1. ` import re  `: Импортирование модуля для работы с регулярными выражениями
2. ` def count_words(filename: str) -> tuple[int, str]:  `: Определение функции count_words с параметром filename, возвращающей кортеж из целого числа (кол-во слов) и строки (самое частое слово).
3. ` with open(filename, 'r', encoding='utf-8') as file:  `: Открытие файла filename для чтения с использованием кодировки utf-8
4. ` words: list[str] = [i for i in [re.sub("[-!.:«»,?""]", '', w.lower()) for w in file.read().split()] if not i == ""]  `: Формирование списка words из слов файла после удаления знаков пунктуации и приведения к нижнему регистру.
5. ` words_count: int = len(words)  `: Подсчет общего количества слов в тексте и присвоение значения переменной words_count.
6. ` d: tuple[str, int] = sorted([(i, words.count(i)) for i in set(words)], key=lambda t: t[1], reverse=True)[0]  `: Формирование кортежа d, содержащего самое частое слово и его количество
7. ` return words_count, d[0]  `: Возврат кортежа с общим количеством слов и самым часто встречающимся словом
8. ` count, word = count_words("Book.txt")  `: Вызов функции count_words для файла "Book.txt" и присвоение результатов переменным count и word
9. ` print(f"Кол-во слов: {count}\n Самое частое слово:'{word}'")  `: Вывод результатов на экран с использованием форматированной строки (f-string).

 ## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
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
```
### Результат.
### Код.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/ind_2_1.png )
### Файл Расходы.txt и консоль с результатами программы
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/ind_2_2.png )

## Выводы
Код выводит три сообщения и просит пользователя выбрать одно из трёх. В зависимости от выбора программа будет выполнять ту или иную функцию. Каждая строчка кода получилась индивидуальной:
1. ` def add_expense(file_name, amount, category): `: Определение функции add_expense для добавления записи о расходах в файл. Параметры: file_name, amount, category
2. ` with open(file_name, 'a', encoding='utf-8') as f: `: Открытие файла для добавления записи с использованием кодировки utf-8.
3. ` f.write(f"Сумма: {amount}, причина: {category}\n") `: Запись строки с суммой и причиной расходов в файл.
4. ` def view_expenses(file_name): `: Определение функции view_expenses для просмотра текущих расходов из файла с параметром file_name
5. ` with open(file_name, 'r', encoding='utf-8') as f: `: Открытие файла для чтения с использованием кодировки utf-8.
6. ` expenses = f.readlines() `: Чтение всех строк из файла и сохранение их в списке expenses.
7. ` for expense in expenses:`: Итерация по каждой строке в списке expenses.
8. ` amount, category = expense.strip().split(',') `: Разделение строки на сумму и причину, используя запятую в качестве разделителя.
9. ` print(f"{amount},  {category}") `: Вывод на экран суммы и причины расходов.
10. ` file_name = "Расходы.txt" `: Задание имени файла.
11. ` while True: `: : Бесконечный цикл для предоставления пользователю выбора.
12. ` print("1. Добавить расходы")  `: 
13. ` print("2. Просмотр текущих расходов") `: 
14. ` print("3. Выход") `: 
15. ` choice = input("Выберите одно из трёх: ")  `: Получение выбора пользователя.
16. ` if choice == "1": `: Условие, если переменная choice равна 1, то переменные amount и category задаются с клавиатуры. Значения, введённые с клавиатуры, становятся значениями параметров функции add_expense
17. ` amount = input("Введите сумму: ") `: 
18. ` category = input("Причина затраты: ") `: 
19. ` add_expense(file_name, amount, category) `: 
20. ` elif choice == "2": `: Иначе, если переменная choice равна 2, то выводит функцию view_expenses
21. ` view_expenses(file_name) `: Иначе, если переменная choice равна 3, то программа завершается
22. ` elif choice == "3": `: 
23. ` break  `: Прерывание цикла при выборе "3. Выход".
24. ` else:  `: Иначе…
25. ` print("Неверный выбор")`: Выводит сообщение

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
### Текст в файле:
Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated.
 ### Ожидаемый результат:
Input file contains:
108 letters
20 words
4 lines

```python
with open('input.txt', 'r') as f:
    lines: list[str] = f.readlines()
    lines_count: int = len(lines)
    words: list[str] = ' '.join(lines).split()
    words_count: int = len(words)
    letters_count: int = sum([len(i.replace('.', "")) for i in words])

    print(f"Input file contains:\n {letters_count} letters\n {words_count} words\n {lines_count} lines")
```
### Результат.
![Меню](https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/ind_3.png)

## Выводы
Код выводит результат, что и требовалось в задании: количество букв латинского алфавита; число слов; число строк. Каждая строчка кода получилась индивидуальной:
1. ` with open('input.txt', 'r') as f:`: Открытие файла 'input.txt' для чтения с использованием контекстного менеджера.
2. ` lines: list[str] = f.readlines()  `: Чтение всех строк из файла и сохранение их в списке lines.
3. ` lines_count: int = len(lines)  `: Подсчет общего количества строк в файле и присвоение значения переменной lines_count.
4. ` words: list[str] = ' '.join(lines).split() `: Объединение всех строк в одну строку, разделение ее на слова и сохранение их в списке words.
5. ` words_count: int = len(words) `: Подсчет общего количества слов в файле и присвоение значения переменной words_count.
6. ` letters_count: int = sum([len(i.replace('.', "")) for i in words]) `: Подсчет общего количества букв во всех словах (удаление точек из слов перед подсчетом) и присвоение значения переменной letters_count.
7. ` print(f"Input file contains:\n {letters_count} letters\n {words_count} words\n {lines_count} lines") `: Вывод информации о содержимом файла на экран с использованием форматированной строки (f-string).

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
### Запрещенные слова:
hello email python the exam wor is
### Предложение для проверки:
Hello, world! Python IS the programming language of thE future. My EMAIL is… 
PYTHON is awesome!!!!
### Ожидаемый результат:
*****, ***ld! ****** ** *** programming language of *** future. My ****** **….
 ****** ** awesome!!!!

```python
import re

forbidden_words: list[str] = []
with open("input_1.txt", "r") as f:
    forbidden_words.extend(f.read().split())

msg: str = input("Ведите предложение или нажмите Enter для предложения по умолчанию: ")

if msg.isspace() or msg == "":
    msg = "Hello, world! Python IS the programming language of thE future. My EMAIL is… \nPYTHON is awesone!!!"

for w in forbidden_words:
    msg = re.sub(w, "*" * len(w), msg, flags=re.IGNORECASE)
print(msg)
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/ind_4.png )

## Выводы
Код выводит сообщение предоставляя выбор пользователю: либо ввести своё предложении или использовать уже готовое. В конечном итоге запрещённые слова заменяет на “*”. Каждая строчка кода получилась индивидуальной:
1. ` import re `: Импорт модуля re для работы с регулярными выражениями.
2. ` forbidden_words: list[str] = []`: Инициализация списка forbidden_words для хранения запрещенных слов.
3. ` with open("input_1.txt", "r") as f:`: Открытие файла "input_1.txt" для чтения с использованием контекстного менеджера.
4. ` forbidden_words.extend(f.read().split()) `: Чтение содержимого файла и добавление слов в список forbidden_words
5. ` msg: str = input("Ведите предложение или нажмите Enter для предложения по умолчанию: ")`: Запрос пользователя на ввод предложения или использование предложения по умолчанию.
6. ` if msg.isspace() or msg == "":`: Проверка на случай ввода только пробелов или пустой строки.
7. ` msg = "Hello, world! Python IS the programming language of thE future. My EMAIL is… \nPYTHON is awesone!!!" `: Установка предложения по умолчанию, если ввод пустой.
8. ` for w in forbidden_words:`: Итерация по запрещенным словам.
9. ` msg = re.sub(w, "*" * len(w), msg, flags=re.IGNORECASE) `: Замена каждого вхождения запрещенного слова в предложении на символ "*" с сохранением регистра.
10. ` print(msg)`: Вывод msg.

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

```python
def search_word_in_file(word, file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        word_lower = word.lower()
        text_lower = text.lower()
        count = text_lower.count(word_lower)
        return count

def main():
    file_name = 'input.txt'
    word_to_find = input("Введите слово для поиска в файле: ")
    count = search_word_in_file(word_to_find, file_name)
    print(f"Слово '{word_to_find}' найдено {count} раз(а) в файле {file_name}")

if __name__ == "__main__":
    main()
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/ind_5_1.png )
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_7/pic/ind_5_2.png )

## Выводы
В задании требовалось придумать и решить задачу. Задача: Напишите код, который будет смотреть сколько раз встретилось введённое пользователем слово в файле input.txt из 3-го самостоятельного задания. Код просит ввести пользователя слово, после чего выводит кол-во раз встречающееся в файле. Каждая строчка кода получилась индивидуальной:
1. ` def search_word_in_file(word, file_name): `: Определение функции search_word_in_file с параметрами word, file_name
2. ` with open(file_name, 'r') as f:`: Открытие файла в режиме чтения с использованием контекстного менеджера.
3. ` text = f.read()`: Чтение содержимого файла и сохранение его в переменной text.
4. ` word_lower = word.lower() `: Преобразование искомого слова в нижний регистр.
5. ` text_lower = text.lower() `: Преобразование всего текста файла в нижний регистр.
6. ` count = text_lower.count(word_lower) `: Подсчет количества вхождений искомого слова в тексте.
7. ` return count `: Возвращение результата поиска.
8. ` def main(): `: Определение функции main	
9. ` file_name = 'input.txt' `: Указание имени файла для поиска.
10. ` word_to_find = input("Введите слово для поиска в файле: ") `: Получение слова для поиска от пользователя.
11. ` count = search_word_in_file(word_to_find, file_name)`: Вызов функции поиска и получение результата.
12. ` print(f"Слово '{word_to_find}' найдено {count} раз(а) в файле {file_name}") `: Вывод результата 
13. ` if __name__ == "__main__": `: Точка входа
14. ` main()  `: Вызов функции main

## Общие выводы по теме
Выводом окончания 7-мой Темы предмета Программная инженерия может послужить изучение природы файлов языка Python и применения полученного в решении самостоятельных заданий. Стало известно, как открывать (open()) и главное закрывать (close()) файлы, чтения данных из файлов (read – чтение всего файла, readline – чтение одной строки, readlines – чтение всех строк), запись данных (write - запись указанной строки, writelines - запись список строк), обработка исключений (try - except) и т.д. Но поскольку я являюсь обладателем операционной системой известной как Windows, мне довелось столкнутся с проблемой, что если в текстовом файле присутствует кириллица, то на выходе программа выдаёт всякую нечитаемую абракадабру. Поэту каждый раз во избежание этого приходится дополнять код (конвертировать в uft-8). Как бы то ни было, надежное управление файлами и обработка исключений помогут в будущем создать более надежные и функциональные программы. 
