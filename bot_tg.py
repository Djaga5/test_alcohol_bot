import telebot
from telebot import types
import webbrowser

TOKEN = '6837772151:AAGPdaQZCmMGz7IuagEn9vQMVkFSMYJE7xw'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Игривое')
    btn2 = types.KeyboardButton('Спокойное')
    btn3 = types.KeyboardButton('Тусовочное')
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id,
                     f'''Привет-привет, <b>{message.from_user.first_name}!</b> Меня зовут <em><u>{bot.get_me().first_name}</u></em>. Я бот-эксперт в выборе алкоголя на новогодний стол. Расскажи, какое у тебя настроение на этот Новый год?''',
                     parse_mode='html', reply_markup=markup)

    stick = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker=stick)

@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://krasnoeibeloe.ru')


@bot.message_handler(content_types=['text'])
def pars_text(message):
    if message.text == 'Игривое':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton('Полегче')
        btn12 = types.KeyboardButton('Покрепче')

        markup.add(btn11, btn12)

        bot.send_message(message.chat.id, 'Сууупер! Прекрасно тебя понимаю)) Давай определимся с крепостью. Хотел бы ты что-то полегче или покрепче?', reply_markup=markup)

    elif message.text == 'Спокойное':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn21 = types.KeyboardButton('Да')
        btn22 = types.KeyboardButton('Обойдусь чаем')

        markup.add(btn21, btn22)

        bot.send_message(message.chat.id, 'Нууу вот :( На Новый год надо отрываться!! Иди пей тогда чай с пустырником! Ну хотяяя.. могу тебе предложить кое-что расслабляющее! Подойдет?', reply_markup=markup)

    elif message.text == 'Тусовочное':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn31 = types.KeyboardButton('Давай полегче')
        btn32 = types.KeyboardButton('Конечно покрепче')

        markup.add(btn31, btn32)

        bot.send_message(message.chat.id, 'Ну мой друг, ты по адресу! Сейчас все устроим! Хотел бы ты что-то полегче или покрепче?', reply_markup=markup)

    elif message.text == 'Полегче':

        inline = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton('До 10%', callback_data='10')
        button_2 = types.InlineKeyboardButton('До 13%', callback_data='13')
        button_3 = types.InlineKeyboardButton('До 20%', callback_data='20')
        button_0 = types.InlineKeyboardButton('Наш веб-сайт', url='https://krasnoeibeloe.ru')

        inline.add(button_1, button_2, button_3, button_0)

        bot.send_message(message.chat.id, 'Таак! Выбери процент содержания алкоголя', reply_markup=inline)

    elif message.text == 'Покрепче':

        inline = types.InlineKeyboardMarkup()
        button_4 = types.InlineKeyboardButton('Россия', callback_data='rus')
        button_5 = types.InlineKeyboardButton('Шотландия', callback_data='sc')
        button_6 = types.InlineKeyboardButton('Франция', callback_data='fr')
        button_0 = types.InlineKeyboardButton('Наш веб-сайт', url='https://krasnoeibeloe.ru')

        inline.add(button_4, button_5, button_6, button_0)

        bot.send_message(message.chat.id, 'Ну ты отважный челик)) Выбери место происхождения напитка', reply_markup=inline)

    elif message.text == 'Да':

        inline = types.InlineKeyboardMarkup()
        button_7 = types.InlineKeyboardButton('Рыба', callback_data='fish')
        button_8 = types.InlineKeyboardButton('Мясо', callback_data='meat')
        button_0 = types.InlineKeyboardButton('Наш веб-сайт', url='https://krasnoeibeloe.ru')

        inline.row(button_7, button_8)
        inline.row( button_0)

        bot.send_message(message.chat.id, 'Ну хорошо, так уж и быть подскажу! Что планируется на твоем новогоднем столе?', reply_markup=inline)

    elif message.text == 'Обойдусь чаем':

        bot.send_message(message.chat.id, 'Мда...Ну и ладно! Пока')

        sticker = open('sticker1.webp', 'rb')
        bot.send_sticker(message.chat.id, sticker)

    elif message.text == 'Давай полегче':

        inline = types.InlineKeyboardMarkup()
        button_9 = types.InlineKeyboardButton('Покрепче', callback_data='strong')
        button_0 = types.InlineKeyboardButton('Наш веб-сайт', url='https://krasnoeibeloe.ru')

        inline.row(button_9)
        inline.row(button_0)

        bot.send_message(message.chat.id, 'Ну и какое тусовочное тут настроение? Не ври мне, выбирай другой вариант ', reply_markup=inline)
    elif message.text == 'Конечно покрепче':

        inline = types.InlineKeyboardMarkup()
        button_10 = types.InlineKeyboardButton('Да', callback_data='yes')
        button_11 = types.InlineKeyboardButton('ДА', callback_data='yes')
        button_0 = types.InlineKeyboardButton('Наш веб-сайт', url='https://krasnoeibeloe.ru')

        inline.row( button_10,button_11)
        inline.row(button_0)

        bot.send_message(message.chat.id, 'Ты точно уверен, что готов прям накидаться?? ', reply_markup=inline)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '10':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton('/start')
        markup.add(btn0)

        bot.send_message(call.message.chat.id, '<b>Пиво или сидр</b> - идеальный вариант! Но рекомендую именно начать новогоднее застолье с этих напитков, а продолжить чем-нибудь покрепче. Если не знаешь, что выбрать начни разговор со мной заново по кнопке ниже',
        parse_mode='html', reply_markup=markup)

        file = open('beer.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=file)

    elif call.data == '13':
        bot.send_message(call.message.chat.id, 'Новый год и без шампанского? Тут прекрасным вариантом будет выбрать <b>розовое игристое, либо классическое</b>. Не забудь поджечь бумажку с желанием и выпить ее вместе с шампанским!',
        parse_mode = 'html')

        file1 = open('champ.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=file1)

    elif call.data == '20':
        bot.send_message(call.message.chat.id, 'Звездой твоего новогоднего стола должно стать <b>Мартини</b>! Рекомендую смешать данный напиток с тоником или соком. И получится вообще пушка! Самый крутой Новый год тебе обеспечен',
        parse_mode = 'html')

        file2 = open('martini.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=file2)

    elif call.data == 'rus':
        bot.send_message(call.message.chat.id, '<b>Водка…</b> Кхм, при всей своей компетентности данный напиток пить на Новый год не рекомендую. Возможны неприятные последствия…',
        parse_mode = 'html')

        file3 = open('vodka.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=file3)

    elif call.data == 'sc':
        bot.send_message(call.message.chat.id, 'Старый добрый <b>Виски</b>. Рекомендую собрать компанию друзей и насладиться этим прекрасным напитком!',
        parse_mode='html')


        file4 = open('whiskey.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=file4)

    elif call.data == 'fr':
        bot.send_message(call.message.chat.id, 'Тебе за 30? Ну что ж… Значит, королем на твоем столе станет <b>коньяк</b>',
        parse_mode='html')

        file5 = open('con.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=file5)

    elif call.data == 'fish':
        bot.send_message(call.message.chat.id, 'Я вижу, что ты настоящий гурман! <b>Белое вино</b> прекрасно сочетается с рыбными блюдами. Советую прикупить бутылочек 5 прозапас))',
        parse_mode='html')

        file6 = open('white.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=file6)

    elif call.data == 'meat':
        bot.send_message(call.message.chat.id, 'Намечается теплый уютный Новый год с бутылочкой <b>красного вина</b>. Надеюсь, ты кайфанешь!',
        parse_mode='html')

        file7 = open('red.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=file7)

    elif call.data == 'strong':
        bot.send_message(call.message.chat.id, 'Супер! Припасись водкой, джином, текилой и ромом. Ведь <b>Лонг-Айленд</b> - это прекрасный способ, чтобы конкретно оторваться в новогоднюю ночь',
        parse_mode='html')

        file8 = open('long.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=file8)

    elif call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Ооо, жесть... Ну твой вариант - это <b>абсент</b>... НО есть вероятность, что Новый год бесследно исчезнет из твоей памяти',
        parse_mode='html')

        file9 = open('abs.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=file9)

bot.polling(non_stop=True)
