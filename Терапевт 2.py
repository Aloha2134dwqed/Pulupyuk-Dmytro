from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Вправи для емоційного здоров'я", callback_data='exercises')],
        [InlineKeyboardButton("Корисні поради", callback_data='tips')],
        [InlineKeyboardButton("Зв'язатися зі спеціалістом", callback_data='specialist')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привіт! Я твій віртуальний терапевт. Обери, чим я можу тобі допомогти:",
        reply_markup=reply_markup
    )

# Обробка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'exercises':
        await query.edit_message_text("Ось декілька вправ для релаксації:\n\n"
                                       "1. Глибоке дихання: вдих на 4 рахунки, затримка на 4 рахунки, видих на 6 рахунків.\n"
                                       "2. Напиши свої емоції в нотатнику.\n"
                                       "3. Прогулянка на свіжому повітрі.")
    elif query.data == 'tips':
        await query.edit_message_text("Корисні поради для збереження емоційного здоров'я:\n\n"
                                       "- Спи не менше 7-8 годин.\n"
                                       "- Уникай перевантажень.\n"
                                       "- Практикуй вдячність – подумай, за що ти вдячний сьогодні.")
    elif query.data == 'specialist':
        await query.edit_message_text("Якщо тобі потрібна допомога спеціаліста, спробуй звернутися до:\n\n"
                                       "- Психолога онлайн\n"
                                       "- Гарячої лінії емоційної підтримки у твоєму регіоні.\n"
                                       "Пам'ятай, це нормально – звертатися за допомогою.")

# Головна функція для запуску бота
def main() -> None:
    application = Application.builder().token("7718412483:AAFy54L_nKJ_Nqc9AG9zvU1od3GwBuXyREs").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущено!")
    application.run_polling()

if __name__ == "__main__":
    main()
