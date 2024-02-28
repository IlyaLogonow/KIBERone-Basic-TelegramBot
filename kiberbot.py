from telebot import types
import random
from random import choice
from bot_token import *
from tutors.tutors import send_tutors

itfacts = ['В Гималаях (юго-западный Китай) живет малая панда (красная панда). В английском языке её называют «Firefox». Это слово вдохновило создателей популярного браузера… вот только на логотип они почему-то поместили красную лису, а не панду.', 'На самом первом логотипе Apple был изображен сидящий под яблоней сэр Исаак Ньютон. Над ним нависает вот-вот готовое упасть яблоко.', 'Компакт-диски (CD) читаются от внутреннего круга до наружного, а записываются с точностью до наоборот.', 'Среднестатистический пользователь компьютера моргает 7 раз в минуту. Нормальный показатель – 12 раз в минуту.', 'Пальцы наборщика текста в среднем за день «пробегают» 20 км.', 'Первый в мире будильник умел звонить только в 4 часа утра.', '30 ноября каждого года отмечается Всемирный день компьютерной безопасности («Computer Security Day“)', 'Радио потребовалось 38 лет, чтобы набрать рыночную аудиторию в 50 млн слушателей, телевидению — 13 лет, iPod — 3 года.', 'Снимок, сделанный самой первой фотокамерой в мире, пришлось бы ждать 8 часов.', 'Skype официально заблокирован в Китае.', 'Текст с экрана читается на 10% медленнее, чем с бумаги.', 'Название популярного Linux-дистрибутива Ubuntu взято из одного из африканских языков. Оно означает «Я из-за тебя».',]

@bot.message_handler(commands=['start']) #стартовая команда
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('💳 Оплата')
    btn2 = types.KeyboardButton('🏫 О KIBERone')
    btn3 = types.KeyboardButton('🧑‍🎓 Ученики')
    markup.add(btn1, btn2, btn3)
    bot.send_photo(message.chat.id, open('kiberone-logo.jpg', 'rb'), '\n\n')
    bot.send_message(message.from_user.id, "Добро пожаловать в школу программирования KIBERone!🙌\nЯ ваш помощник - KiberBot, и я здесь, чтобы помочь вам узнать больше о нашей школе, произвести оплату и предоставить полезные ресурсы для изучения программирования.\n\nВыберите нужный вам раздел ⬇", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    #Оплата
    if message.text == '💳 Оплата':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔗 Оплата по ссылке')
        btn2 = types.KeyboardButton('🤳 Оплата по QR-коду')
        btn3 = types.KeyboardButton('👉 Оплата прямо из Telegram')
        btn4 = types.KeyboardButton('🔙 Вернуться')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_photo(message.chat.id, open('qrPayment/art.png', 'rb'), '\n\n')
        bot.send_message(message.from_user.id, 'Если вы родитель и хотите оплатить обучение, вы можете воспользоваться двумя способами: по ссылке или с помощью QR-кода.\n\nЕсли вы выбрали оплату по ссылке, вам достаточно перейти по ссылке, которую я вам пришлю, и следовать инструкциям на экране. Вы можете оплатить обучение с помощью банковской карты или любого другого удобного способа.\n\nЕсли вы выбрали оплату с помощью QR-кода, вам достаточно отсканировать код, который я вам пришлю, с помощью вашего мобильного телефона и следовать инструкциям на экране. Вы можете оплатить обучение с помощью электронного кошелька или любого другого удобного способа.\n\nОбе опции оплаты безопасны и надежны. Все ваши данные защищены и не доступны третьим лицам.', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔗 Оплата по ссылке':
        bot.send_message(message.chat.id, 'https://securecardpayment.ru/sc/ggpAExpVjMweMjqd')

    elif message.text == '🤳 Оплата по QR-коду':
        caption = ['Для оплаты необходимо:',
                   '1️⃣ Сохранить фото/сделать скриншот кода',
                   '2️⃣ Зайти в приложение банка ',
                   '3️⃣ Выбрать оплату по QR коду',
                   '4️⃣ Загрузить фото ',
                   '5️⃣ Ввести нужную сумму',
                   ]
        bot.send_photo(message.chat.id, open('qrPayment/QR_code_payment.jpg', 'rb'), '\n\n'.join(caption))

    elif message.text == '👉 Оплата прямо из Telegram':
        bot.send_message(message.chat.id, 'В разработке)')
        # payment_token = 'Здесь должен быть токен Sber'
        # title = 'Оплата занятий'
        # description = 'Оплата занятий замесяц в школе KiberOne'
        # invoice = 'invoice'
        # currency = 'RUB'
        # prices = [types.LabeledPrice(title, 5500 * 100)]
        # bot.send_invoice(message.chat.id, title, description, invoice, payment_token, currency, prices)

    elif message.text == '🔙 Вернуться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('💳 Оплата')
        btn2 = types.KeyboardButton('🏫 О KIBERone')
        btn3 = types.KeyboardButton('🧑‍🎓 Ученики')
        markup.add(btn1, btn2, btn3)
        bot.send_photo(message.chat.id, open('kiberone-logo.jpg', 'rb'), '\n\n')
        bot.send_message(message.from_user.id, "Добро пожаловать в школу программирования KIBERone!🙌\nЯ ваш помощник - KiberBot, и я здесь, чтобы помочь вам узнать больше о нашей школе, произвести оплату и предоставить полезные ресурсы для изучения программирования.\n\nВыберите нужный вам раздел ⬇", reply_markup=markup)
        

    #О Школе
    elif message.text == '🏫 О KIBERone':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('👩🏻‍🏫 Тьюторы')
        btn2 = types.KeyboardButton('🎬 Социальные-Медиа')
        btn3 = types.KeyboardButton('👀 Ты этого точно не знал!')
        btn4 = types.KeyboardButton('🔙 Вернуться')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "👋 Информация о школе KIBERone", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

    elif message.text == '🔙 Вернуться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('💳 Оплата')
        btn2 = types.KeyboardButton('🏫 О KIBERone')
        btn3 = types.KeyboardButton('🧑‍🎓 Ученики')
        markup.add(btn1, btn2, btn3)
        bot.send_photo(message.chat.id, open('kiberone-logo.jpg', 'rb'), '\n\n')
        bot.send_message(message.from_user.id, "Добро пожаловать в школу программирования KIBERone!🙌\nЯ ваш помощник - KiberBot, и я здесь, чтобы помочь вам узнать больше о нашей школе, произвести оплату и предоставить полезные ресурсы для изучения программирования.\n\nВыберите нужный вам раздел ⬇", reply_markup=markup)

    #Рандомные факты
    elif message.text == '👀 Ты этого точно не знал!':
        for i in range(1):
            bot.send_message(message.from_user.id, random.choice(itfacts))

    #ТЬЮТОРЫ
    elif message.text == '👩🏻‍🏫 Тьюторы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        msg_id = message.from_user.id
        bot.send_message(msg_id, '👩🏻‍🏫 Список тьюторов:', reply_markup=markup, parse_mode='Markdown')
        send_tutors(msg_id)

    #СОЦИАЛЬНЫЕ МЕДИА
    elif message.text == '🎬 Социальные-Медиа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('📷 Вк')
        markup.add(btn01, btn1)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    #ВЫХОД В ГЛАВНОЕ МЕНЮ
    elif message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('👩🏻‍🏫 Тьюторы')
        btn2 = types.KeyboardButton('🎬 Социальные-Медиа')
        btn3 = types.KeyboardButton('👀 Ты этого точно не знал!')
        btn4 = types.KeyboardButton('🔙 Вернуться')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, "👋 Информация о школе KIBERone", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

    #Ученики
    elif message.text == '🧑‍🎓 Ученики':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📅 Расписание')
        btn2 = types.KeyboardButton('📁 Проекты и мероприятия')
        btn3 = types.KeyboardButton('📚 Знания')
        btn4 = types.KeyboardButton('💻 Навигация профессий')
        btn5 = types.KeyboardButton('👀 Ты этого точно не знал!')
        btn6 = types.KeyboardButton('🔙 Вернуться')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, "👋 Информация о резиденте KIBERone", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')
    
    elif message.text == '🔙 Вернуться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('💳 Оплата')
        btn2 = types.KeyboardButton('🏫 О KIBERone')
        btn3 = types.KeyboardButton('🧑‍🎓 Ученики')
        markup.add(btn1, btn2, btn3)
        bot.send_photo(message.chat.id, open('kiberone-logo.jpg', 'rb'), '\n\n')
        bot.send_message(message.from_user.id, "Добро пожаловать в школу программирования KIBERone!🙌\nЯ ваш помощник - KiberBot, и я здесь, чтобы помочь вам узнать больше о нашей школе, произвести оплату и предоставить полезные ресурсы для изучения программирования.\n\nВыберите нужный вам раздел ⬇", reply_markup=markup)

    #РАСПИСАНИЕ
    elif message.text == '📅 Расписание':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Расписание на ул. Василия Гольцова, 10')
        btn2 = types.KeyboardButton('Расписание на ул. Республики, 160')
        btn3 = types.KeyboardButton('Расписание на Солнечный проезд, 24')
        btn4 = types.KeyboardButton('Расписание на ул. Тихий проезд, 1')
        btn5 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, open('Weekly-class-schedule.png', 'rb'), '\n\n')
        bot.send_message(message.from_user.id, 'У меня есть полезная функция расписания занятий, которая позволяет вам посмотреть расписание занятий любой точки нашей школы.📅\n\nС помощью этой функции вы можете выбрать любую точку нашей школы, которая вас интересует, и посмотреть расписание занятий на текущую неделю.👏\n\n', reply_markup=markup, parse_mode='Markdown')

    #ПРОЕКТЫ И МЕРОПРИЯТИЯ
    elif message.text == '📁 Проекты и мероприятия':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню ученика')
        btn1 = types.KeyboardButton('🔎 Олимпиада KIBERone - Scratch')
        btn2 = types.KeyboardButton('🔎 Олимпиада KIBERone - Kodu Game Lab')
        btn3 = types.KeyboardButton('🔎 Олимпиада KIBERone - Roblox Studio')
        btn4 = types.KeyboardButton('🔎 Скоро будут')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn4)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)
    
    #ЗНАНИЯ
    elif message.text == '📚 Знания':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню ученика')
        btn1 = types.KeyboardButton('📚 Книги')
        btn2 = types.KeyboardButton('📚 Фильмы')
        markup.add(btn01, btn1, btn2)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)
    
    elif message.text == '📚 Книги':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Список книг', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📚 Фильмы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Список фильмов', reply_markup=markup, parse_mode='Markdown')

    #НАВИГАЦИЯ ПРОФЕССИЙ
    elif message.text == '💻 Навигация профессий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('🔙 Главное меню ученика')
        btn1 = types.KeyboardButton("🛠 Frontend-developer")
        btn2 = types.KeyboardButton('🛠 Backend-developer')
        btn3 = types.KeyboardButton('🛠 Game-developer')
        btn4 = types.KeyboardButton('🛠 Тестировщик')
        btn5 = types.KeyboardButton('🛠 Разработчик искусственного интеллекта')
        btn6 = types.KeyboardButton('🛠 3d художник')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == '🛠 Frontend-developer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    
    elif message.text == '🛠 Backend-developer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🛠 Game-developer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    
    elif message.text == '🛠 Тестировщик':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')
    
    elif message.text == '🛠 Разработчик искусственного интеллекта':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🛠 3d художник':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню ученика')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Тут должно быть описание', reply_markup=markup, parse_mode='Markdown')

    #ГЛАВНОЕ МЕНЮ УЧЕНИКА
    elif message.text == '🔙 Главное меню ученика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📅 Расписание')
        btn2 = types.KeyboardButton('📁 Проекты и мероприятия')
        btn3 = types.KeyboardButton('📚 Знания')
        btn4 = types.KeyboardButton('💻 Навигация профессий')
        btn5 = types.KeyboardButton('👀 Ты этого точно не знал!')
        btn6 = types.KeyboardButton('🔙 Вернуться')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, "👋 Информация о резиденте KIBERone", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')
    

bot.polling(none_stop=True, interval=0) 