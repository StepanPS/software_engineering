# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме #8 выполнил:
- Пичкуренко Степан Сергеевич
- АИС-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

Работу проверили:
- к.э.н., доцент Панов М.А.
## Лабораторная работа №1
### Создайте класс "Car" с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car:  # Класса Car
    def __init__(self, make, model):  # Определение конструктора класса, который принимает параметры make и model
        self.make = make  # Присвоение значения make атрибуту make объекта self
        self.model = model   # Присвоение значения model атрибуту model объекта self


my_car = Car("Toyota", "Corolla")  # Создание объекта my_car класса Car с аргументами "Toyota" и "Corolla"
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_8/pic/lab_1.png)

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину "поехать". Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:  # Класса Car
    def __init__(self, make, model):  # Определение конструктора класса, который принимает параметры make и model
        self.make = make  # Присвоение значения make атрибуту make объекта self
        self.model = model  # Присвоение значения model атрибуту model объекта self

    def drive(self):  # Метод drive с объектом self
        print(f"Driving the {self.make} {self.model}")  # Выводит сообщение со значением атрибутов make и model объекта self


my_car = Car("Toyota", "Corolla")  # Создание объекта my_car класса Car с аргументами "Toyota" и "Corolla"
my_car.drive()  # Вызов метода drive у объекта my_car
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_8/pic/lab_2.png)

## Лабораторная работа №3
### Создайте новый класс "ElectricCar" с методом "charge" и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться.
```python
class Car:  # Класса Car
    def __init__(self, make, model):  # Определение конструктора класса, который принимает параметры make и model
        self.make = make  # Присвоение значения make атрибуту make объекта self
        self.model = model  # Присвоение значения model атрибуту model объекта self

    def drive(self):  # Метод drive с объектом self
        print(f"Driving the {self.make} {self.model}")  # Выводит сообщение со значением атрибутов make и model объекта self


my_car = Car("Toyota", "Corolla")  # Создание объекта my_car класса Car с аргументами "Toyota" и "Corolla"
my_car.drive()  # Вызов метода drive у объекта my_car


class ElectricCar(Car):  # Дочерний класс ElectricCar класса Car
    # Определение конструктора класса, который принимает объект self параметры make, model и battery_capacity
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)  # Функция super() вызывает метод инициализации __init__ из родительского класса
        # Присвоение значения battery_capacity атрибуту battery_capacity объекта self
        self.battery_capacity = battery_capacity

    def charg(self):  # Метод charg с объектом self
        # Выводит сообщение со значением атрибутов make, model и battery_capacity объекта self
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

# Создание объекта my_electric_car дочернего класса ElectricCar с аргументами "Tesla", "Model S", 75
my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()  # Вызов метода drive у объекта my_electric_car
my_electric_car.charg()  # Вызов метода charg у объекта my_electric_car
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_8/pic/lab_3.png)

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:  # Класса Car
    def __init__(self, make, model):  # Определение конструктора класса, который принимает параметры make и model
        self._make = make  # Присвоение значения make защищённому атрибуту _make объекта self
        self.__model = model  # Присвоение значения model приватному атрибуту __model объекта self

    def drive(self):  # Метод drive с объектом self
        # Выводит сообщение со значением атрибутов _make и __model объекта self
        print(f"Driving the {self._make} {self.__model}")


my_car = Car("Toyota", "Corolla") # Создание объекта my_car класса Car с аргументами "Toyota" и "Corolla"
print(my_car._make)  # Выводит значение защищённого атрибута _make
# print(my_car.__model)  # Ошибка! Приватный атрибут не доступен
my_car.drive()  # Вызов метода drive у объекта my_car```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_8/pic/lab_4.png)

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс "Shape", а также еще два класса "Rectangle" и "Circle". Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Shape:  # Класс Shape
    def area(self):  # метод area с объектом self
        pass  # Пустой блок кода


class Rectangle(Shape):  # Дочерний класс Rectangle класса Shape
    # Определение конструктора класса, который принимает параметры width и height
    def __init__(self, width, height):
        self.width = width  # Присвоение значения width атрибуту width объекта self
        self.height = height  # Присвоение значения height атрибуту height объекта self

    def area(self):  # Метод area с объектом self
        return self.width * self.height  # Возвращает умножение присвоенных значений атрибутов width и height


class Circle(Shape):  # Дочерний класс Circle класса Shape
    def __init__(self, radius):  # Определение конструктора класса, который принимает параметр radius
        self.radius = radius  # Присвоение значения radius атрибуту radius объекта self

    def area(self):  # Метод area с объектом self
        return 3.14 * self.radius * self.radius  # Возвращает 3.14 умноженное на квадрат значения атрибута radius

# Массив shapes, в котором дочерним классам, а точнее, их параметрам присвоены числовые значения
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:  # Цикл перебирает элементы массива shapes
    print(shape.area())  # Выводит результат вызова метода area() для каждой фигуры в списке shapes
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_8/pic/lab_5.png)

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Literature:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book = Literature("War of the Worlds", "Herbert Wells")
print(book.title)
print(book.author)
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_8/pic/ind_1.png)

## Выводы
Код выводит два сообщения. Каждая строчка кода получилась индивидуальной:
1. ` class Literature: `: Класс Literature 
2. ` def __init__(self, title, author): `: Определение конструктора класса, который принимает параметры title и author
3. ` self.title = title  `: Присвоение значения title атрибуту title объекта self
4. ` self.author = author  `: Присвоение значения author атрибуту author объекта self
5. ` book = Literature("War of the Worlds", "Herbert Wells")`: Создание объекта book класса Literature с аргументами "War of the Worlds" и"Herbert Wells"
6. ` print(book.title)`: Выводит значение параметра title объекта book
7. ` print(book.author)`: Выводит значение параметра author объекта book

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Literature:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        print(f"Я недавно прочёл книгу: '{self.title}'. Её написал  {self.author}.")


book = Literature("War of the Worlds", "Herbert Wells")
book.read()
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_8/pic/ind_2.png)

## Выводы
Код выводит одно сообщение. Каждая строчка кода получилась индивидуальной:
1. ` class Literature:`: Комментарии с 1 по 4 и 8 эквивалентны комментариям с 1 по 4 и 8 первого задания
2. ` def __init__(self, title, author):`: 
3. ` self.title = title`: 
4. ` self.author = author `: 
5. ` def read(self): `: Метод read с объектом self
6. ` print(f"Я недавно прочёл книгу: '{self.title}'. Её написал  {self.author}.")`: Вывод информации о содержимом файла на экран с использованием форматированной строки (f-string).
7. ` book = Literature("War of the Worlds", "Herbert Wells")`: 
8. ` book.read()`: вызов метода read у объекта book

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Literature:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        print(f"Я недавно прочёл книгу: '{self.title}'. Её написал  {self.author}.")


book = Literature("War of the Worlds", "Herbert Wells")
book.read()


class Film(Literature):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def fiction(self):
        return f"Нет же! '{self.title}' это фильм режиссёра {self.author} выпущенный в {self.genre} году."


fiction_book = Film("War of the Worlds", "Steven Spielberg", 2005)
print(fiction_book.fiction())
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_8/pic/ind_3.png)

## Выводы
Код выводит два сообщения. Каждая строчка кода получилась индивидуальной:
1. ` class Literature:`: Комментарии с 1 по 9 эквивалентны комментариям с 1 по 9 второго задания
2. ` def __init__(self, title, author): `: 
3. `  `: 
4. ` self.title = title`: 
5. ` self.author = author `: 
6. ` def read(self):`: 
7. ` print(f"Я недавно прочёл книгу: '{self.title}'. Её написал  {self.author}.")`: 
8. ` book = Literature("War of the Worlds", "Herbert Wells")`: 
9. ` book.read()`: 
10. ` class Film(Literature):`: Дочерний класс Film класса Literature
11. ` def __init__(self, title, author, genre):`: Определение конструктора класса, который принимает объект self и параметры title, author, genre
12. ` super().__init__(title, author) `: Функция super() вызывает метод инициализации __init__ из родительского класса
13. ` self.genre = genre `: Присвоение значения genre атрибуту genre объекта self
14. `def fiction(self):`: Метод fiction с объектом self
15. ` return f"Нет же! '{self.title}' это фильм режиссёра {self.author} выпущенный в {self.genre} году." `: Вывод информации о содержимом файла на экран с использованием форматированной строки (f-string).
16. `fiction_book = Film("War of the Worlds", "Steven Spielberg", 2005)`: Создание объекта fiction_book  дочернего класса Film с аргументами "War of the Worlds", "Steven Spielberg", 2005
17. ` print(fiction_book.fiction())`: Выводит объект fiction_book  метода fiction

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Literature:
    def __init__(self, title, author, date):
        self.title = title
        self._author = author
        self.__date = date

    def read(self):
        print(f"Я недавно прочёл книгу: '{self.title}'. Её написал {self._author} в {self.__date} году.")


book = Literature("War of the Worlds", "Herbert Wells", 1898)
book.read()
print(book.title)
print(book._author)
print(book.__date)
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_8/pic/ind_4.png)

## Выводы
Код выводит три сообщения и ошибку показывающую, что атрибут является приватным. Каждая строчка кода получилась индивидуальной:
1. ` class Literature:`: Класс Literature
2. ` def __init__(self, title, author, date):`: Определение конструктора класса, который принимает параметры title, author, date
3. ` self.title = title`: Присвоение значения title публичному атрибуту title объекта self
4. ` self._author = author`: Присвоение значения author защищённому атрибуту _author объекта self
5. ` self.__date = date`: Присвоение значения date приватному атрибуту __date объекта self
6. ` def read(self):`: Метод read с объектом self 
7. ` print(f"Я недавно прочёл книгу: '{self.title}'. Её написал {self._author} в {self.__date} году.")`: Вывод информации о содержимом файла на экран с использованием форматированной строки (f-string).
8. ` book = Literature("War of the Worlds", "Herbert Wells", 1898)`: Создание объекта book класса Literature с аргументами "War of the Worlds", "Herbert Wells", 1898
9. ` book.read()`: Вызов метода read у объекта book
10. ` print(book.title)`: Выводит значение публичного атрибута title
11. ` print(book._author) `: Выводит значение защищённого атрибута _author
12. ` print(book.__date)`: Выводит значение приватного атрибута __date

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Magazine:
    def __init__(self, title, publisher):
        self.title = title
        self.publisher = publisher

    def display_info(self):
        return f"Журнал'{self.title}' издаётся {self.publisher}."


class Literature:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Книга '{self.title}' написана {self.author}."


class Bookshelf:
    def show_item_info(self, item):
        return item.display_info()


fiction_book = Literature("War of the Worldsd", "Herbert Wells")
magazine = Magazine("National Geographic", "National Geographic Partners")
bookshelf = Bookshelf()

print(bookshelf.show_item_info(fiction_book))
print(bookshelf.show_item_info(magazine))
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_8/pic/ind_5.png)

## Выводы
Код выводит два сообщения с найденными значениями. Каждая строчка кода получилась индивидуальной:
1. ` class Magazine:`: Класс Magazine
2. ` def __init__(self, title, publisher): `: Определение конструктора класса, который принимает параметры title, publisher
3. ` self.title = title `: Присвоение значения title атрибуту title объекта self
4. ` def display_info(self): `: Метод display_info
5. ` return f"Журнал'{self.title}' издаётся {self.publisher}." `: Возвращает информацию о содержимом файла на экран с использованием форматированной строки (f-string).
6. ` class Literature:`: Класс Literature
7. `def __init__(self, title, author): `: Определение конструктора класса, который принимает параметры title, author
8. ` self.title = title `: Присвоение значения title атрибуту title объекта self
9. ` self.author = author `: Присвоение значения author атрибуту author объекта self
10. ` def display_info(self): `: Метод display_info
11. ` return f"Книга '{self.title}' написана {self.author}." `: Возвращает информацию о содержимом файла на экран с использованием форматированной строки (f-string). 
12. ` class Bookshelf:`:  Класс Bookshelf
13. `def show_item_info(self, item): `: Метод show_item_info с объектом self и параметром item
14. ` return item.display_info()`: Возвращает параметр item метода display_info
15. ` fiction_book = Literature("War of the Worldsd", "Herbert Wells")`: Создание объекта fiction_book класса Literature с аргументами "War of the Worlds", "Herbert Wells"
16. ` magazine = Magazine("National Geographic", "National Geographic Partners") `: Создание объекта magazine класса Magazine с аргументами "National Geographic", "National Geographic Partners"
17. ` bookshelf = Bookshelf() `: Переменной bookshelf присвоено значение: функция Bookshelf()
18. ` print(bookshelf.show_item_info(fiction_book)) `: Выводит сообщение: значение переменной bookshelf метода show_item_info объекта fiction_book
19. ` print(bookshelf.show_item_info(magazine)) `: Выводит сообщение: значение переменной bookshelf метода show_item_info объекта magazine

## Общие выводы по теме 
В ходе изучения Темы 8 были изучены основы объектно-ориентированного программирования языка Python. В результате стали известны классы и объекты, а также основные элементы ООП, такие, как инкапсуляция, наследование и полиморфизм и их взаимоотношение между собой. Итог таков, что работа по введению в объектно-ориентированное программирование на языке Python позволила понять основы ООП и применить их в решении самостоятельных работ. Этот подход к программированию предоставляет эффективные инструменты для создания модульного, гибкого и масштабируемого кода.
