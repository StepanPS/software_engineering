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
