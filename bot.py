from telegram import MessageEntity, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

sponsors = ['@dilik_zel']

buttons = ReplyKeyboardMarkup([['Продвигать✅', 'Вип программа🔥'], ['Что такое ТикТок❔❓'], [
    'Как работает бот❓❔'], ['Любые вопросы / Предложения по боту📝']], resize_keyboard=False)


def unknown_msg(update, context):
    update.message.reply_html(
        'Unknown message', reply_markup=buttons)


def start(update, context):

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
        '''<b>Вы пригласили xx людей 🥰</b>Чтобы получить вип и попасть к нам в закрытую группу надо пригласить 7 человек.
После того как пригласите 7 человек, отправьте скринь @DeeL_TG он дабавит вас в закрытую группу. 💥
Ваша реферальная ссылка: РЕФ ссылка
скопируйте эту ссылку и отправьте друзьям➡️''',
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
    keyboard = [[InlineKeyboardButton("Проверить подписку✅", callback_data='1')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    print(update.message.from_user.id)
    update.message.reply_html(
        '''Упс.Чтобы мы продвигали твой аккаунт подпишись пожалуйста на наших спонсоров.\n
<b>1)</b> {}
\nИ мы проверим твой аккаунт в течении 24 часов и начнем продвигать твой аккаунт'''.format(sponsors[0])
        , reply_markup=reply_markup)
    return '1'


def checkJoined(update, context):
    print(update.message.from_user.userid)
    # update.effective_chat.get_chat_member(sponsors[0], update.message.from_user.first_name)


updater = Updater('1604509578:AAFUMndjSSMbHz8TsLtlLnDLXA1imr0KoQU', use_context=True)
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        1: [
            MessageHandler(Filters.regex('^(Продвигать✅)$'), promote),
            MessageHandler(Filters.regex('^(Вип программа🔥)$'), vipProgram),
            MessageHandler(Filters.regex('^(Что такое ТикТок❔❓)$'), whatIsTikTok),
            MessageHandler(Filters.regex('^(Как работает бот❓❔)$'), howBotWorks),
            MessageHandler(Filters.regex('^(Любые вопросы / Предложения по боту📝)$'), anyQuestions),
            MessageHandler(Filters.entity(MessageEntity.URL), linkHandler),
            CallbackQueryHandler(checkJoined, pattern='^(' + str(1) + ')$')
        ]
    },
    fallbacks=[MessageHandler(Filters.text, unknown_msg)]
)

updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()
