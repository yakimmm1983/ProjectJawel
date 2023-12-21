from Settings import Settings
from telegram import Update,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder,ContextTypes,CommandHandler,filters,MessageHandler
import DTO.ClientDto
async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    button = [[KeyboardButton("/help")]]
    await update.effective_message.reply_text(
        text="Начало работы",
        reply_markup=ReplyKeyboardMarkup(button,one_time_keyboard=True,resize_keyboard=True)
        )
async def help(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(text="Помощь")
async def RegUser(update:Update,context:ContextTypes.DEFAULT_TYPE):
    recive = update.message.text
    phone= ""
    name=""
    second_name=""
    email=""
    third_name=""
    # recive = "phone:phone,name:name,first:first,second:second"
    recive = recive.split(", ")
    #recive = ["phone","name","first","second"]

    phone = recive[0]
    name = recive[1]
    second_name=recive[2]
    email=recive[3]
    if len(recive) > 4:
        third_name=recive[4]
    else:
        pass
    DTO.ClientDto.RegistraionUser(phone = phone,
                                  first_name=name,
                                  second_name=second_name,
                                  email=email,
                                  third_name=third_name)
    await update.effective_message.reply_text(text="Пользователь добавлен")
async def registrationUser(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        text="Введите номер телефона, имя, фамилию, электронную почту, отчество через запятую")
    infoHandler = MessageHandler(filters.TEXT,RegUser)
    application.add_handler(infoHandler)
if __name__ == '__main__':
    application = ApplicationBuilder().token(Settings.token).build()
    startHandler = CommandHandler("start",start)
    helpHandler = CommandHandler("help",help)
    application.add_handler(helpHandler)
    application.add_handler(startHandler)
    regHandler = CommandHandler("regUser", registrationUser)
    application.add_handler(regHandler)
    print("Bot started")
    application.run_polling()
