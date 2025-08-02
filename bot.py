from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

TOKEN = "7728323563:AAG9n4eygpME7HJthPGQICM62Y_Wzlu2AlU"

# Состояния диалога
WHATSAPP, AGE, HEIGHT, WEIGHT, BUST, WAIST, HIPS, COUNTRY, ENGLISH, TATTOO, EXPERIENCE = range(11)

# Стартовая команда
def start(update, context):
    update.message.reply_text("Привет! Заполни, пожалуйста, анкету.\nУкажи свой WhatsApp номер:")
    return WHATSAPP

def whatsapp(update, context):
    context.user_data['WhatsApp'] = update.message.text
    update.message.reply_text("Возраст:")
    return AGE

def age(update, context):
    context.user_data['Возраст'] = update.message.text
    update.message.reply_text("Рост, см:")
    return HEIGHT

def height(update, context):
    context.user_data['Рост'] = update.message.text
    update.message.reply_text("Вес, кг:")
    return WEIGHT

def weight(update, context):
    context.user_data['Вес'] = update.message.text
    update.message.reply_text("Бюст:")
    return BUST

def bust(update, context):
    context.user_data['Бюст'] = update.message.text
    update.message.reply_text("Талия, см:")
    return WAIST

def waist(update, context):
    context.user_data['Талия'] = update.message.text
    update.message.reply_text("Бёдра, см:")
    return HIPS

def hips(update, context):
    context.user_data['Бёдра'] = update.message.text
    update.message.reply_text("Страна резидента:")
    return COUNTRY

def country(update, context):
    context.user_data['Страна'] = update.message.text
    update.message.reply_text("Уровень английского (A1, A2, B1, B2, C1, C2, другой):")
    return ENGLISH

def english(update, context):
    context.user_data['Английский'] = update.message.text
    update.message.reply_text("Татуировки/пирсинг (Есть/Нет):")
    return TATTOO

def tattoo(update, context):
    context.user_data['Татуировки/пирсинг'] = update.message.text
    update.message.reply_text("Опыт (Есть/Нет):")
    return EXPERIENCE

def experience(update, context):
    context.user_data['Опыт'] = update.message.text
    
    # Формирование ответа
    answers = "\n".join([f"{key}: {value}" for key, value in context.user_data.items()])
    update.message.reply_text("Спасибо! Вот твои ответы:\n" + answers)
    
    # Здесь можно отправить ответы администратору или сохранить их в БД
    print("Новая анкета:", context.user_data)

    return ConversationHandler.END

def cancel(update, context):
    update.message.reply_text("Анкета отменена.")
    return ConversationHandler.END

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            WHATSAPP: [MessageHandler(Filters.text & ~Filters.command, whatsapp)],
            AGE: [MessageHandler(Filters.text & ~Filters.command, age)],
            HEIGHT: [MessageHandler(Filters.text & ~Filters.command, height)],
            WEIGHT: [MessageHandler(Filters.text & ~Filters.command, weight)],
            BUST: [MessageHandler(Filters.text & ~Filters.command, bust)],
            WAIST: [MessageHandler(Filters.text & ~Filters.command, waist)],
            HIPS: [MessageHandler(Filters.text & ~Filters.command, hips)],
            COUNTRY: [MessageHandler(Filters.text & ~Filters.command, country)],
            ENGLISH: [MessageHandler(Filters.text & ~Filters.command, english)],
            TATTOO: [MessageHandler(Filters.text & ~Filters.command, tattoo)],
            EXPERIENCE: [MessageHandler(Filters.text & ~Filters.command, experience)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

