# Тема 8. Концепции и принципы ООП
Отчет по Теме #9 выполнил:
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
### Допустим, что вы решили оригинально и немного странно познакомится с человеком. Для этого у вас должен быть написан свой класс на Python, который будет проверять угадал ваше имя человек или нет. Для этого создайте класс, указав в свойствах только имя. Дальше создайте функцию ＿ init (), а в ней сделайте проверку на то угадал человек ваше имя или нет. Также можете проверить что будет, если в этой функции указав атрибут, который не указан в вашем классе, например, попробуйте вызвать фамилию.

```python
class Ivan:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Иван':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, я Иван!"


person1 = Ivan('Алексей')
person2 = Ivan('Иван')
print(person1.name)
print(person2.name)

person2.surename = 'Петров'
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_9/pic/lab_1.png)

## Лабораторная работа №2
### Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения. Для этого вам нужно написать класс, в котором будет определяться изменили ли состав мороженого или нет. В этом классе реализуйте метод, выводящий на печать «Мороженое с {ТОППИНГ}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое». При этом программа должна воспринимать как топпинг только атрибуты типа string.

```python
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None
    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print('Обычное мороженное')
icecream = Icecream()
icecream.composition()
icecream = Icecream('шоколадом')
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_9/pic/lab_2.png)

## Лабораторная работа №3
### Петя - начинающий программист и на занятиях ему сказали реализовать икапсу…что-то. А вы хороший друг Пети и ко всему прочему прекрасно знаете, что икапсу…что-то - это инкапсуляция, поэтому решаете помочь вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают. Также вас необходимо объяснить Пете почему на скриншоте ниже в консоли выводится ошибка.

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):  # установка значения атрибута
        self._value = value

    def get_value(self):  # получение значения атрибута
        return self._value

    def del_value(self):
        del self._value  # удаление атрибута

    value = property(get_value, set_value, del_value, "Свойство value")


obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_9/pic/lab_3.png)

## Лабораторная работа №4
### Вам прекрасно известно, что кошки и собаки являются млекопитающими, но компьютер этого не понимает, поэтому вам нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи "наследования" объяснить компьютеру что кошки и собаки - это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга.

```python
class Mammal:
    className = 'Mammal'


class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'


class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'


dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds}")
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_9/pic/lab_4.png)

## Лабораторная работа №5
### На разных языках здороваются по-разному, но суть остается одинаковой, люди друг с другом здороваются. Давайте вместе с вами реализуем программу с полиморфизмом, которая будет описывать всю суть первого предложения задачи. Для этого мы можем выбрать два языка, например, русский и английский и написать для них отдельные классы, в которых будет в виде атрибута слово, которым здороваются на этих языках. А также напишем функцию, которая будет выводить информацию о том, как на этих языках здороваются. Заметьте, что для решения поставленной задачи мы использовали декоратор @staticmethod, поскольку нам не нужны обязательные параметры-ссылки вроде self.

```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")


class English:
    @staticmethod
    def greeting():
        print("Hello")


def greet(language):
    language.greeting()


ivan = Russian()
greet(ivan)
john = English()
greet(john)
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_9/pic/lab_5.png)	

## Задание
### Задание:
Класс Tomato:
1) Создайте класс Tomato
2) Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
3) Создайте метод ＿ init (), внутри которого будут определены два динамических свойства: index (передается параметром) и state (принимает первое значение из словаря states). После написания этого блока кода в комментарии к нему укажите какими являются эти два свойства
4) Создайте метод grow(), который будет переводить томат на следующую стадию созревания
5) Создайте метод is_ripe(), который будет проверять, что томат созрел
Класс TomatoBush:
1) Создайте класс TomatoBush
2) Определите метод ＿init＿ (), который будет принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса Tomato. Данный список будет храниться
внутри динамического свойства tomatoes
3) Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
4) Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми.
5) Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
Класс Gardener:
1) Создайте класс Gardener
2) Создайте метод ＿init＿(), внутри которого будут определены два динамических свойства: name (передается параметром, является публичным) и _plant (принимает объект класса TomatoBush). После написания этого блока кода в комментарии к нему укажите какими являются эти два свойства
3) Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
4) Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все, то садовник собирает урожай. Если нет, то метод печатает предупреждение
5) Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству
```python
class Tomato:
    states: tuple[str, ...] = ("none", "bloom", "green", "red")

    def __init__(self, index: int):
        self._index: int = index
        self.__stage: int = 0
        self._state: str = Tomato.states[self.__stage]

    def grow(self) -> None:
        self.__stage += 1
        self.__stage %= len(Tomato.states)
        self._state: str = Tomato.states[self.__stage]

    def is_ripe(self) -> bool:
        return self.__stage == len(Tomato.states) - 1


class TomatoBush:
    def __init__(self, count: int):
        self.__tomatoes: list[Tomato, ...] = [Tomato(i) for i in range(count)]

    def grow_all(self) -> None:
        for t in self.__tomatoes:
            t.grow()

    def all_are_ripe(self) -> bool:
        return all([t.is_ripe() for t in self.__tomatoes])

    def give_away_all(self) -> None:
        self.__tomatoes.clear()


class Gardener:
    def __init__(self, name: str, plant: TomatoBush):
        self.name: str = name
        self._plant: TomatoBush = plant

    def work(self) -> None:
        self._plant.grow_all()

    def harvest(self) -> bool:
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран")
            return True
        else:
            print("Растение еще не созрело")
            return False

    @staticmethod
    def knowledge_base() -> None:
        print("Справка")
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_9/pic/classes.png)
## Выводы
Каждая строчка кода получилась индивидуальной:
1. `class Tomato:`: класс Tomato
2. ` states: tuple[str, ...] = ("none", "bloom", "green", "red")`: Статическое поле states, представляющее различные стадии созревания помидора
3. `def __init__(self, index: int):`: Конструктор класса, принимающий индекс и инициализирующий атрибуты
4. ` self._index: int = index`: Индекс помидора
5. `self.__stage: int = 0 `: Приватный атрибут, представляющий текущую стадию созревания
6. `self._state: str = Tomato.states[self.__stage]`: Атрибут, представляющий текущее состояние помидора
7. `def grow(self) -> None:`: Метод для перехода к следующей стадии созревания
8. `self.__stage += 1`: 
9. `self.__stage %!=(MISSING) len(Tomato.states) `: Обеспечиваем зацикли
10. `class TomatoBush:`: Класс TomatoBush
11. `def __init__(self, count: int):`:
12. `self.__tomatoes: list[Tomato, ...] = [Tomato(i) for i in range(count)]`: В конструкторе создается список объектов класса `Tomato` в количестве, заданном параметром `count`.
13. `def grow_all(self) -> None:`: Метод `grow_all` вызывает метод `grow` для каждого объекта класса `Tomato` в списке.
14. `for t in self.__tomatoes:`:
15. `t.grow()`:
16. `def all_are_ripe(self) -> bool:`: Метод `all_are_ripe` возвращает True, если все помидоры в списке вызывают метод `is_ripe()` и возвращают True.
17. `return all([t.is_ripe() for t in self.__tomatoes])`:
18. `def give_away_all(self) -> None:`: Метод `give_away_all` очищает список помидоров, представляя собой передачу всех помидоров.
19. `self.__tomatoes.clear()`:
20. `class Gardener:`: Класс Gardener
21. `def __init__(self, name: str, plant: TomatoBush):`: Определение конструктора класса "gardener" с двумя параметрами: "name" (имя садовника, должно быть строкой) и "plant" (томатный куст, тип данных " TomatoBush ")
22. `self.name: str = name`: Инициализация атрибута "name" класса "gardener" значением параметра "name"
23. `self._plant: TomatoBush = plant`: Инициализация атрибута "_plant" класса "gardener" значением параметра "plant"
24. `def work(self) -> None:`: Определение метода "work" класса "gardener" без параметров, который возвращает "none"
25. `self._plant.grow_all()`:Вызов метода "grow_all" у объекта "self._plant" класса "tomatobush"
26. `def harvest(self) -> bool:`: Определение метода "harvest" класса "gardener" без параметров, который возвращает логическое значение (bool)
28. `if self._plant.give_away_all()`:Проверка, являются ли все плоды объекта "self._plant" класса "tomatobush" созревшими
29. `print("Урожай собран")`: Вывод сообщения "урожай собран" 
30. `return True`: возврат значения "true"
31. `else:`: Иначе…
32. `print("Растение еще не созрело")`: Вывод сообщения "растение еще не созрело" 
33. `return False`: возврат значения "false"
34. `@staticmethod`: Декоратор
35. `def knowledge_base() -> None:`: Определение статического метода "knowledge_base" класса "gardener" без параметров, который возвращает "none"
36. `print("Справка")`: Вывод сообщения "справка"

## Тест №1
### Вызовите справку по садоводству
```python
from ind.classes import Gardener

if __name__ == '__main__':
    Gardener.knowledge_base()
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_9/pic/test_1.png)

## Выводы
Код выводит  сообщения с найденными значениями. Каждая строчка кода получилась индивидуальной:
1. ` from ind.classes import Gardener`: Импортируем модуль gardener из пакета ind.classes
2. ` if __name__ == '__main__':`: Точка входа
3. ` Gardener.knowledge_base()`: Вызываем функцию knowledge_base() из модуля Gardener    

## Тест №2
### Создайте объекты классов TomatoBush и Gardener
```python
from ind.classes import TomatoBush, Gardener

if __name__ == '__main__':
    bush = TomatoBush(10)
    gardener = Gardener("Пётр", bush)
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_9/pic/test_2.png)

## Выводы
Код выводит сообщения с найденными значениями. Каждая строчка кода получилась индивидуальной:
1. ` from ind.classes import TomatoBush, Gardener`: Импортируем модуль TomatoBush  и Gardener из пакета ind.classes
2. ` if __name__ == '__main__':`: Точка входа
3. ` bush = TomatoBush(10)`: Создание экземпляра класса TomatoBush с аргументом 10 и присвоение его переменной bush.
4. ` gardener = Gardener("Пётр", bush)`: Создание экземпляра класса Gardener с аргументами "Пётр" и bush и присвоение его переменной gardener.

## Тест №3
### Используя объект класса Gardener, поухаживайте за кустом с помидорами
```python
from ind.classes import TomatoBush, Gardener

if __name__ == '__main__':
    bush = TomatoBush(10)
    gardener = Gardener("Пётр", bush)
    gardener.work()
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_9/pic/test_3.png )

## Выводы
Код выводит сообщения с найденными значениями. Каждая строчка кода получилась индивидуальной:
1. ` gardener.work()`: Вызов метода work() у объекта gardener, который, предположительно, будет заботиться о кусте помидоров.

## Тест №4
### Попробуйте собрать урожай, когда томаты еще не дозрели. Продолжайте ухаживать за ними
```python
from ind.classes import TomatoBush, Gardener

if __name__ == '__main__':
    bush = TomatoBush(10)
    gardener = Gardener("Пётр", bush)
    for _ in range(4):
        gardener.harvest()
        gardener.work()
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_9/pic/test_4.png)

## Выводы
Код выводит сообщения с найденными значениями. Каждая строчка кода получилась индивидуальной:
1. ` gardener.harvest()`: Вызов метода harvest () у объекта gardener

## Тест №5
### Соберите урожай
```python
from ind.classes import TomatoBush, Gardener

if __name__ == '__main__':
    bush = TomatoBush(10)
    gardener = Gardener("Пётр", bush)
    for _ in range(3):
        gardener.work()
    gardener.harvest()
```
### Результат.
![Меню]( https://github.com/StepanPS/software_engineering/blob/Tema_9/pic/test_5.png )

## Выводы
Код выводит сообщения с найденными значениями. Каждая строчка кода получилась индивидуальной:
1. ` for _ in range(3):`: цикл будет выполняться три раза, используя переменную `_`

## Общие выводы по теме 
В ходе выполнения лабораторной работы по теме "Python. Концепции и принципы ООП" были изучены основные принципы объектно-ориентированного программирования (ООП) и их применение на языке Python. В процессе работы были рассмотрены следующие ключевые концепции:классы и объекты, инкапсуляция, наследование: Механизм, позволяющий создавать новые классы на основе существующих. наследование, полиморфизм. Можно отметить, что использование принципов ООП в языке программирования Python способствует созданию более читаемого, структурированного и масштабируемого кода. ООП позволяет лучше организовывать программные проекты, делая их более поддерживаемыми и расширяемыми в будущем.
