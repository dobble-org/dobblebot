import cv2
import numpy as np
import io
from .state import States
from dobblebot.services.yolov5 import YoloService
from io import BytesIO

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

class DobbleBot:
    def __init__(self, detection_service: YoloService) -> None:
        self._detection_service = detection_service

    async def on_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        await update.message.reply_html(
            f'Hi {user.mention_html()}!' 
            'I am Dobble Bot and I can help you detect icons on Dobble cadrs. Just send me a photo!',
            reply_markup=ForceReply(selective=True),
        )
    
    async def on_stop(self, update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_html(
            f'Ok, Bye!',
            reply_markup=ForceReply(selective=True),
        )

    async def process_image(self, update, context):
        image_file = await context.bot.get_file(update.message.photo[-1].file_id)
        bytes =  await image_file.download_as_bytearray()
        data_as_np_array = np.frombuffer(bytes, np.uint8)
        image_data = cv2.imdecode(data_as_np_array, cv2.IMREAD_COLOR)   
        processed_results = self._detection_service.detect(image_data)
        _, buffer = cv2.imencode('.bmp', processed_results.render()[0].astype(np.uint8))

        buffer_storage = io.BytesIO(buffer)

        cv2.imdecode(np.frombuffer(buffer_storage.getbuffer(), np.uint8), -1)

        await update.message.reply_photo(
            buffer_storage,
            reply_markup=ForceReply(selective=True),
        )
