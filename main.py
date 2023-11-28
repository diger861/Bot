import telebot
from telebot import types

bot = telebot.TeleBot('6661107624:AAE89fGbNcKD_TufgkDTONK1vPv3-7zMazA')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Внести карту наблюдений')
        btn2 = types.KeyboardButton('Сообщить о инциденте')
        btn3 = types.KeyboardButton('Зарегистрировать активность лидера')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup)  # ответ бота


    elif message.text == 'Внести карту наблюдений':
        bot.send_message(message.from_user.id,
                         'Я очень рад, что вы решили внести вклад в безопасность, скорее переходите по\n \n' + '[ссылке](https://docs.google.com/forms/d/e/1FAIpQLSfwqQ9pHpVAqpduOzZtuORi7dn-GngzBaNO5eIKETdIoh_YtQ/viewform)',
                         parse_mode='Markdown')

    elif message.text == 'Сообщить о инциденте':
        bot.send_message(message.from_user.id, 'Сообщить о инциденте Вы сможете ' + '[ссылке](hse@techofs.com)',
                         parse_mode='Markdown')

    elif message.text == 'Зарегистрировать активность лидера':
        bot.send_message(message.from_user.id,
                         'Зарегистрировать активность по ' + '[ссылке](https://docs.google.com/forms/d/e/1FAIpQLScs6qgw4-Oa6k9GLGLriWuVAYGCxFFNSoZsPVzPf3olOUycqw/viewform)',
                         parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть
