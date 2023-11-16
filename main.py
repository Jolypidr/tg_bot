import telebot
from telebot import types

bot = telebot.TeleBot('6922632992:AAHzzlTofSORccU1JFuoFxOQmAhwXcpvlxo')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Добрый день", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Начать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Заказать')
        btn2 = types.KeyboardButton('Каталог')
        btn3 = types.KeyboardButton('Вопрос')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Выберете раздел меню', reply_markup=markup) #ответ бота


    elif message.text == 'Заказать': bot.send_message(message.from_user.id,'Наш менеджер свяжется с Вами в течении нескольких минут!', parse_mode='Markdown') 
    elif message.text == 'Каталог': bot.send_message(message.from_user.id, '[ссылке](https://telegra.ph/Instrukciya-POIZON-11-11)', parse_mode='Markdown') 
    elif message.text == 'Вопросы': bot.send_message(message.from_user.id, 'Чтобы бы вы хотели узнать?', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть