# Тема: Итоговый проект. 
Отчет по Теме # выполнил:
- Пичкуренко Степан Сергеевич
- АИС-21-1

Работу проверили:
- к.э.н., доцент Панов М.А.

## Итоговый проект
### Telegram бот позволяющий конвертировать валюту.
```python
import telebot
from telebot import types
from currency_converter import CurrencyConverter

c = CurrencyConverter()
amount = 0
bot = telebot.TeleBot('6811650230:AAEXhbUPDLgo4USKdm0EcEEYFxf0udAZtwU')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Доброго времени суток. Введите вашу сумму.')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат.')
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        m = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton('RUB/USD', callback_data='RUB/USD')
        button2 = types.InlineKeyboardButton('CNY/JPY', callback_data='CNY/JPY')
        button3 = types.InlineKeyboardButton('RUB/CNY', callback_data='RUB/CNY')
        button4 = types.InlineKeyboardButton('RUB/EUR', callback_data='RUB/EUR')
        button5 = types.InlineKeyboardButton('GBP/USD', callback_data='GBP/USD')
        button6 = types.InlineKeyboardButton('Пользовательские значения', callback_data='else')
        m.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, 'Выберите пару валют (пример валют:EUR – евро, JPY – японская иена, '
                                          'GBP – фунт стерлингов, AUD – австралийский доллар, CNY – китайская юань)',
                         reply_markup=m)
    else:
        bot.send_message(message.chat.id, 'Сумма должна быть больше 0.')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.split('/')
        res = c.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}.')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите валюты через "/"')
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = c.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается: {round(res, 2)}.')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Что-то не так.')
        bot.register_next_step_handler(message, summa)


bot.polling(none_stop=True)
```
### Результат.
![Меню](https://github.com/StepanPS/software_engineering/blob/Final_Project/pic/final_project.png)


## Выводы
1.	` import telebot`: Импортируем библиотеку telebot
2.	` from telebot import types`: Импортируем из модуля telebot конкретный класс – types (кнопки)
3.	` from currency_converter import CurrencyConverter`: Импортируем из модуля currency_converter конкретный класс – CurrencyConverter (конвертация)
4.	` c = CurrencyConverter()`: Переменной присваиваем класс CurrencyConverter
5.	` amount = 0`:
6.	`bot = telebot.TeleBot('6811650230:AAEXhbUPDLgo4USKdm0EcEEYFxf0udAZtwU') `: создание экземпляра класса TeleBot с указанием токена бота, полученного при регистрации.

7.	`@bot.message_handler(commands=['start']) `: вызывается декорированная функция и входящее сообщение передается в качестве аргумента.
8.	`def start(message): `: функция с параметром 
9.	`bot.send_message(message.chat.id, 'Доброго времени суток. Введите вашу сумму.') `: функция send_message позволяет боту отправить сообщение 
10.	` bot.register_next_step_handler(message, summa)`: функция register_next_step_handler с двумя аргументами message и функцией summa

11.	`def summa(message): `: функция с параметром 
12.	` global amount`: объявление переменной amount как глобальной, чтобы ее значение можно было изменять внутри функции.
13.	try:
14.	` amount = int(message.text.strip())`: переменной присваивается значение – это сообщение от пользователя целочисленное число(функция int). Функция strip удаляет пробелы
15.	except ValueError:
16.	` bot.send_message(message.chat.id, 'Неверный формат.')`:
17.	`if amount > 0: `: если переменная amount больше 0
18.	`m = types.InlineKeyboardMarkup(row_width=1)`: создается объект m типа InlineKeyboardMarkup (встроенная клавиатура), который представляет собой элемент встроенной клавиатуры. Параметр
19.	`  button1 = types.InlineKeyboardButton('RUB/USD', callback_data='rub/usd')`: объект одной кнопки, с параметром которая именуется RUB/USD, аргументом  callback_data – это строка с данными, отправляемые боту в ответном запросе при нажатии кнопки
20.	` button3 = types.InlineKeyboardButton('Пользовательские значения', callback_data='else')`:
21.	` m.add(button1, button2, button3)`: добавление на клавиатуру наших кнопок
22.	`bot.send_message(message.chat.id, 'Выберите пару валют ', reply_markup=m) `: reply_markup параметр функции send_message выводит сообщение и клавиатуру
23.	else:
24.	` bot.send_message(message.chat.id, 'Сумма должна быть больше 0.')`:
25.	`bot.register_next_step_handler(message, summa) `:

26.	`@bot.callback_query_handler(func=lambda call: True) `: вызывается декорированная функция callback_query_handler (позволяет обрабатывать пользовательские действия, связанные с нажатием кнопок клавиатуры) с параметром func=lambda call: True(функция lambda которая всегда True, всегда реагирует на нажатие кнопок)
27.	`def callback(call): `: функция при нажатии на кнопку, параметр
28.	` if call.data != 'else':`: Условие, которое проверяет, что поле data запроса не равно 'else'.
29.	` values = call.data.upper().split('/')`: Значение поля data из запроса преобразуется в верхний регистр(функции upper) и затем разбивается по разделителю '/'.
30.	`res = c.convert(amount, values[0], values[1]) `: объект c, функция convert, кол-во amount, первый, второй элемент
31.	` bot.polling(none_stop=True)`: Позволяет продолжать боту работать, даже если возникнут ошибки

