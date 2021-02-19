
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

buttons = ReplyKeyboardMarkup([['Продвигать✅', 'Вип программа🔥'], ['Что такое ТикТок❔❓'], [
                              'Как работает бот❓❔'], ['Любые вопросы', 'Предложения по боту📝']], resize_keyboard=False)

def unknownMsg(update, context):
    update.message.reply_html(
        'Unknown message', reply_markup=buttons)
    return 1


def start(update, context):
    update.message.reply_html(
        '''<b>Привет, {}</b>,\nя помогу раскрутить твой аккаунт в TikTok, а также буду присылать тебе крутые штуки по 
продвижению.\n\nДля начала, если не трудно, прочитай как работает бот. 📝'''.format(update.message.from_user.first_name)
        , reply_markup=buttons)
    return 1


def promote(update, context):
    update.message.reply_html(
        '''Отлично! Пришли мне ссылку на свой аккаунт или ссылку на свое видео в TikTok😉\n\n(ссылка ташлайди)\n\nУпс. 
Чтобы мы продвигали твой аккаунт подпишись пожалуйста на наших спонсоров.'''
        , reply_markup=buttons)


def vipProgramm(update, context):
    update.message.reply_html(
        '''<b>Вы приглашаете 7 людей, а мы делаем анализ вашего аккаунта и даем советы по улучшению. 
И попадете в нашу закрытую группу. Личная беседа с создателем бота.</b>''',
        reply_markup=buttons)


def whatIsTikTok(update, context):
    update.message.reply_html(
        '<b>TikTok</b> - это площадка, где можно легко стать известным👩🏻‍🦳 и заработать деньги💰. А наша команда может помочь в этом деле.📌',
        reply_markup=buttons)


def howBotWorks(update, context):
    update.message.reply_html(
        '''Есть много правил в Тиктоке, которые нельзя нарушать❗️, и о которых нигде не пишут🖊. Мы поможем тебе удачно продвинуть твой тикток и даже начать зарабатывать не нем.
💰Практически каждые 2 дня📌, мы будем присылать тебе крутые идеи/новости/новые правила в тиктоке.➡️\n
Как мы помогаем попасть в рекомендации❓\n
Наша команда👥  с блогерами миллионниками будем смотреть твои посты, делиться, комментировать. Это заметит Тикток и будет продвигать твои видео в реки.\n
Как работает вип программа❓ 🔥\n
Вы приглашаете 7 людей, а мы делаем анализ вашего аккаунта и даем советы по улучшению. И попадете в нашу закрытую группу. Личная беседа с создателем бота.\n
Всех в реки ➡️😊
''',
        reply_markup=buttons)


def anyQuestions(update, context):
    update.message.reply_html(
        'Любые вопросы/предложения по боту📝\n\nПо любым вопросам обращайтесь к ➡️ @маниюезрим',
        reply_markup=buttons)


def suggestionsToBot(update, context):
    update.message.reply_html(
        'suggestions',
        reply_markup=buttons)


updater = Updater(
    '1604509578:AAFUMndjSSMbHz8TsLtlLnDLXA1imr0KoQU', use_context=True)
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        1: [
            MessageHandler(Filters.regex('^(Продвигать✅)$'), promote),
            MessageHandler(Filters.regex('^(Вип программа🔥)$'), vipProgramm),
            MessageHandler(Filters.regex(
                '^(Что такое ТикТок❔❓)$'), whatIsTikTok),
            MessageHandler(Filters.regex(
                '^(Как работает бот❓❔)$'), howBotWorks),
            MessageHandler(Filters.regex('^(Любые вопросы)$'), anyQuestions),
            MessageHandler(Filters.regex(
                '^(Предложения по боту📝)$'), suggestionsToBot),
        ]
    },
    fallbacks=[MessageHandler(Filters.text, unknownMsg)]
)

updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()
