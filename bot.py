import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

# Habilitar el registro para depuración
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Token de tu bot (reemplaza con tu token real)
TOKEN = "8123049058:AAEaEtMVhlMRKZ04FsGPbi5DNiNVnw2cRlM"

# Función que maneja el comando /start
async def start(update: Update, context: CallbackContext):
#creacion del boton menu
    keyboard = [[InlineKeyboardButton("Menú", callback_data="menu")],
                 [InlineKeyboardButton("Soporte", callback_data="soporte")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "¡Hola! Soy el bot de Ktm's Store. Puede hacer la solicitud de compra con nosotros",
        reply_markup=reply_markup
    )
async def menu(update: Update, context: CallbackContext):
#       Muestra todas las opciones del menu
    await update.callback_query.message.reply_text("Ejecutando menu")



#Funcion que lee los click en los botones
async def button_callback(update: Update, context:CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == "menu":
        await query.message.reply_text("Ejecutando....")
        await menu(update, context)

    elif query.data == "actualizar":
        await query.message.reply_text("Ejecutando....")
        await actualizar(update, context)






async def actualizar(update: Update, context: CallbackContext):
#       Funcion que envia las ultimas actualizaciones del bot
    await update.message.reply_text(
        "Este bot aun está en desarrollo, La ultima actualizacion fue:\n Añadir el boton Menú")

def main():
    # Crear la aplicación con el token del bot
    app = Application.builder().token(TOKEN).build()

    # Registrar el manejador del comando /start
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("actualizar", actualizar))
    app.add_handler(CommandHandler("menu", menu))

    #Registrar el manejador de botones
    app.add_handler(CallbackQueryHandler(button_callback))

    # Iniciar el bot en modo polling
    app.run_polling()

if __name__ == "__main__":
    main()
