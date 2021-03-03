from telegram import MessageEntity, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

sponsors = ['@dilik_zel']
users = []
usersId = []
links = {}

buttons = ReplyKeyboardMarkup([['Продвигать✅', 'Вип программа🔥'], ['Что такое ТикТок❔❓'], [
    'Как работает бот❓❔'], ['Любые вопросы / Предложения по боту📝']], resize_keyboard=False)


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
        '''<b>Привет, {}</b>,\nя помогу раскрутить твой аккаунт в TikTok, а также буду присылать тебе крутые штуки по
продвижению.\n\nДля начала, если не трудно, прочитай как работает бот. 📝'''.format(update.message.from_user.first_name)
        , reply_markup=buttons)
    return 1


def promote(update, context):
    update.message.reply_html(
        '''Отлично! Пришли мне ссылку на свой аккаунт или ссылку на свое видео в TikTok😉''',
        reply_markup=buttons)


def vipProgram(update, context):
    update.message.reply_html(
        '''🥰Чтобы получить вип и попасть к нам в закрытую группу надо пригласить 7 человек.
После того как пригласите 7 человек, отправьте скрин @DeeL_TG он вас добавит в закрытую группу. 💥️''',
        reply_markup=buttons)


def whatIsTikTok(update, context):
    update.message.reply_html(
        '<b>TikTok</b> - это площадка, где можно легко стать известным👩🏻‍🦳 и заработать деньги💰. А наша команда '
        'может помочь в этом деле.📌',
        reply_markup=buttons)


def howBotWorks(update, context):
    update.message.reply_html(
        '''Есть много правил в Тиктоке, которые нельзя нарушать❗️, и о которых нигде не пишут🖊. Мы поможем тебе удачно продвинуть твой тикток и даже начать зарабатывать не нем.
💰Практически каждые 2 дня📌, мы будем присылать тебе крутые идеи/новости/новые правила в тиктоке.➡️\n
Как мы помогаем попасть в рекомендации❓\n
Наша команда👥  с блогерами миллионниками будем смотреть твои посты, делиться, комментировать. Это заметит Тикток и будет продвигать твои видео в реки.\n
Как работает вип программа❓ 🔥\n
Вы приглашаете 7 людей, а мы делаем анализ вашего аккаунта и даем советы по улучшению. И попадете в нашу закрытую группу. Личная беседа с создателем бота.\n
Всех в реки ➡️😊''',
        reply_markup=buttons)


def anyQuestions(update, context):
    update.message.reply_html(
        'По любым вопросам обращайтесь к ➡️ @DeeL_TG',
        reply_markup=buttons)


def linkHandler(update, context):
    a = ""
    for i in range(len(sponsors)):
        a += "{}) {}\n".format(i + 1, sponsors[i])
    keyboard = [[InlineKeyboardButton("Проверить подписку✅", callback_data='1')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_html(
        '''Упс.Чтобы мы продвигали твой аккаунт подпишись пожалуйста на наших спонсоров.\n
{}
\nИ мы проверим твой аккаунт в течении 24 часов и начнем продвигать твой аккаунт'''.format(a)
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
        query.edit_message_text(text=f'''Ты еще не подписался на спонсорские каналы
Подпишись на них и проверь подписку снова''')
    else:
        query.edit_message_text(text=f'''Отлично 🔥🔥
Мы в течении 24 часов начнем продвигать твой аккаунт в рекомендации. А ты пока не теряй время и публикуй классные ролики в Тик-Ток.''')
    # return 1


# updater = Updater('1604509578:AAFUMndjSSMbHz8TsLtlLnDLXA1imr0KoQU', use_context=True)
updater = Updater('1612017020:AAF-ArUOd_ax12KcXYQbcqpwzSv8XGHEVt8', use_context=True)
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        1: [
            MessageHandler(Filters.regex('^(Продвигать✅)$'), promote),
            MessageHandler(Filters.regex('^(Вип программа🔥)$'), vipProgram),
            MessageHandler(Filters.regex('^(Что такое ТикТок❔❓)$'), whatIsTikTok),
            MessageHandler(Filters.regex('^(Как работает бот❓❔)$'), howBotWorks),
            MessageHandler(Filters.regex('^(Любые вопросы / Предложения по боту📝)$'), anyQuestions),
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
