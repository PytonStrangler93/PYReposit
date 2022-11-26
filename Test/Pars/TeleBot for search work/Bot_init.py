import telebot as t
from Work_ua import list
from Rabota_ua import list2


bot = t.TeleBot('5434044927:AAGXRe1KEWlHOHGS5mjMm__qFgwVslpnEds')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Привет, я помогаю найти вакансии за последние сутки с сайтов Work.ua и rabota.ua.
                                        \n Команда для Work - /work
                                        \n Команда для rabota - /rabota
                                        \n Команда для обоих сервисов - /alljob
                                        \n Можешь кликнуть по команде или набрать вручную!
                                         ''')


@bot.message_handler(commands=['work'])
def work(message):
    mess = '\n'.join(list)
    bot.send_message(
        message.chat.id, f"<b>Вакансии WORK:</b>\n{mess}", parse_mode='html')


@bot.message_handler(commands=['rabota'])
def work(message):
    mess2 = '\n'.join(list2)
    bot.send_message(
        message.chat.id, f"<b>Вакансии RABOTA:</b>\n{mess2}", parse_mode='html')


bot.polling(none_stop=True)
