import telebot
from cfg import *
from extentions import *



BOT_TOKEN = '6620367933:AAHJwVEvvdtBRhjbb717fF-RByy88A3U0CA'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start',])
def starter(message: telebot.types.Message):
    bot.send_message(message.chat.id, '''Это - Для работы введите: валюты, которые хотите конвертировать и сумму к конвертации.\
Пример : 'BTC USD 10'. Другие доступные команды бота : /help, /values''')

@bot.message_handler(commands=['help'])
def help (message: telebot.types.Message):
    text = 'Бот для конвертации валют. Бот округляет сумму до целого числа'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступны следующие валюты: '
    for key in keys.keys():
        text ='\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise Convertexception("Не правильный ввод!")
        quote, base, amount_str = values
        amount = float(amount_str)
        total_base = CryptoConverter.convert(quote, base, amount)
    except Convertexception as e:
        bot.reply_to(message, f'Ошибка!!#№#!№#!\n{e}')

    except Exception:
        bot.reply_to(message, "Команда не обработана")
    else:
        result = total_base * amount
        text = f"Цена {amount} {quote} в {base} = {result}"
        bot.send_message(message.chat.id, text)

bot.polling()


