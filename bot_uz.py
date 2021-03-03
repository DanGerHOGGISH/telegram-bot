from telegram import MessageEntity, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

sponsors = ['@dil_zil']
users = []
usersId = []
links = {}

buttons = ReplyKeyboardMarkup([['Rekka Chiqish✅', 'Vip Programma🔥'], ["Tik Tok nima o'zi❔❓"], [
    'Bot qanday ishlaydi❓❔'], ["Har qanday savol / takliflar bo'yicha📝"]], resize_keyboard=False)


def unknown_msg(update, context):
    msg = update.message.text
    if msg.startswith("/addNewSponsorToThisBot") and len(msg) > len("/addNewSponsorToThisBot") + 2:
        small_msg = msg[len('/addNewSponsorToThisBot') + 1:]
        if small_msg[0] != "@":
            context.bot.send_message(chat_id=update.message.from_user.id, text="@ qoyiw oldiga esingdan chiqdimi?:)")
        else:
            sponsors.append(small_msg)

    elif msg.startswith("/removeSponsorFromThisBot"):
        try:
            sponsors.remove(msg[len('/removeSponsorFromThisBot') + 1:])
        except:
            context.bot.send_message(chat_id=update.message.from_user.id, text="bunaqa admin yo'qku :)")

    elif msg.startswith("/sendAllUsersAd") and len(msg) > len("/sendAllUsersAd") + 2:
        ad = msg[len("/sendAllUsersAd") + 1:]
        for i in range(len(usersId)):
            context.bot.send_message(chat_id=usersId[i], text=ad)

    elif msg.startswith("/whichUsers"):
        all_users = ""
        for i in range(len(users)):
            all_users += users[i] + "-" + str(usersId[i]) + "\n"
            update.message.reply_html(all_users, reply_markup=buttons)
    elif msg.startswith("/howManyUsersIHave"):
        update.message.reply_html(len(usersId), reply_markup=buttons)

    elif msg.startswith("/peopleJoinedToSponsor") and len(msg) > len("/peopleJoinedToSponsor") + 2:
        name = msg[len("/peopleJoinedToSponsor") + 1:]
        joined_users = []
        for i in range(len(usersId)):
            a = context.bot.get_chat_member(name, usersId[i])
            if a["status"] != "left":
                joined_users.append(users[i])
        str_joined_users = ""
        for user in joined_users:
            str_joined_users += user + "\n"
        update.message.reply_html(str_joined_users, reply_markup=buttons)

    elif msg.startswith("/howManyPeopleJoinedToSponsor") and len(msg) > len("/howManyPeopleJoinedToSponsor") + 2:
        name = msg[len("/howManyPeopleJoinedToSponsor") + 1:]
        joined_users = []
        for i in range(len(usersId)):
            a = context.bot.get_chat_member(name, usersId[i])
            if a["status"] != "left":
                joined_users.append(users[i])
        update.message.reply_html(len(joined_users), reply_markup=buttons)

    else:
        pass


def start(update, context):
    if update.message.from_user.id != 440255990:
        users.append(update.message.from_user.first_name)
        usersId.append(update.message.from_user.id)
    update.message.reply_html(
        '''<b>Salom, {}</b>,\nMen sizning TikTok hisobingizni targ'ib qilishda yordam beraman va sizga ajoyib narsalarni yuboraman rag'batlantirish.
Birinchidan, qiyin bo'lmasa, bot qanday ishlashini o'qing. 📝'''.format(update.message.from_user.first_name),
        reply_markup=buttons)
    return 1


def promote(update, context):
    update.message.reply_html(
        '''Yaxshi! Menga Tiktokdagi videoingiz ssilkasini yuboring😉''',
        reply_markup=buttons)


def vipProgram(update, context):
    update.message.reply_html(
        '''🥰VIP olish va yopiq guruhimizga kirish uchun siz 7 kishini taklif qilishingiz kerak.
7 kishini taklif qilgandan so'ng, @DeeL_TG ga skrin junating, u sizni yopiq guruhga qo'shadi.''',
        reply_markup=buttons)


def whatIsTikTok(update, context):
    update.message.reply_html(
        '''<b>TikTok</b> - osongina taniqli👩🏻‍🦳‍   bo'lishingiz va pul ishlashingiz mumkin bo'lgan joy💰. Va 
        bizning jamoamiz bu masalada yordam berishi mumkin.📌''',
        reply_markup=buttons)


def howBotWorks(update, context):
    update.message.reply_html(
        '''Tiktokda buzilmasligi kerak bo'lgan va hech qayerda yozilmagan ko'plab qoidalar mavjud❗️. Biz sizga tiktok-ni muvaffaqiyatli targ'ib qilishda va hatto undan daromad olishni boshlashda yordam beramiz.
💰 deyarli har 2 kunda📌, sizga tiktokda ajoyib g'oyalar / yangiliklar / yangi qoidalar yuboramiz .➡️

Sizga taniqli bo'lishingizga qanday yordam beramiz❓

Bizning jamoamiz👥 millionlab odamlar bilan bloggerlar bilan, biz sizning yozuvlaringizni ko'rib chiqamiz, baham ko'ramiz, fikr bildiramiz. Bu Tiktok tomonidan sezilib qoladi va videolaringiz rekda tarqaladi.
''',
        reply_markup=buttons)


def anyQuestions(update, context):
    update.message.reply_html(
        "Har qanday savol / takliflar bo'yicha 📝",
        reply_markup=buttons)


def linkHandler(update, context):
    a = ""
    for i in range(len(sponsors)):
        a += "{}) {}\n".format(i + 1, sponsors[i])
    keyboard = [[InlineKeyboardButton("Tekshirish✅", callback_data='1')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_html(
        '''Ups. Sizning akkauntingizni rekka chiqarishimiz uchun, sponsorlarga obuna bo'ling.\n
{}
\nVa biz sizning akkauntingizni 24 soat ichida tekshirib, rekka olib chiqamiz'''.format(a)
        , reply_markup=reply_markup)
    # return 2


def checkJoined(update, context):
    query = update.callback_query
    query.answer()
    is_joined = True
    for sponsor in sponsors:
        try:
            a = context.bot.get_chat_member(sponsor, update.effective_user["id"])
            if a["status"] == "left":
                is_joined = False
                break
        except:
            print("exception occurred")
            sponsors.remove(sponsor)
    if not is_joined:
        query.edit_message_text(text=f'''Hali obuna bo'lmagansiz''')
    else:
        query.edit_message_text(text=f'''Zo'r 🔥🔥
Tavsiya bo'yicha sizning hisobingizni 24 soat ichida targ'ib qilishni boshlaymiz. Bu orada vaqtni sarflamang va Tik-Tok-da ajoyib videolarni nashr eting''')
    # return 1


# updater = Updater('1604509578:AAFUMndjSSMbHz8TsLtlLnDLXA1imr0KoQU', use_context=True)
updater = Updater('1655854049:AAGP1v9iwqtCdDoAik6BYHKvbpSrteovQZA', use_context=True)
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        1: [
            MessageHandler(Filters.regex('^(Rekka Chiqish✅)$'), promote),
            MessageHandler(Filters.regex('^(Vip Programma🔥)$'), vipProgram),
            MessageHandler(Filters.regex("^(Tik Tok nima o'zi❔❓)$"), whatIsTikTok),
            MessageHandler(Filters.regex('^(Bot qanday ishlaydi❓❔)$'), howBotWorks),
            MessageHandler(Filters.regex("^(Har qanday savol / takliflar bo'yicha📝)$"), anyQuestions),
            # MessageHandler(Filters.entity(MessageEntity.URL), linkHandler),
            CallbackQueryHandler(checkJoined)
        ]
    },
    fallbacks=[
        MessageHandler(Filters.entity(MessageEntity.URL), linkHandler),
        MessageHandler(Filters.text, unknown_msg)
    ]
)

updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()
