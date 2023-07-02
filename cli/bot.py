import os

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


from dobblebot.bot import DobbleBot, States
from dobblebot.services.yolov5 import YoloService


def main(token: str):
    yolo_weights = os.environ['YOLO_WEIGHTS']
    detection_service = YoloService(yolo_weights)
    bot = DobbleBot(detection_service)
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler('start', bot.on_start))
    application.add_handler(CommandHandler('stop', bot.on_stop))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.PHOTO, bot.process_image))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
    main(TOKEN)