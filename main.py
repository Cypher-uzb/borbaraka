from aiogram import Bot, Dispatcher, executor, types
from config import bot_token
import logging
logging.basicConfig(level=logging.INFO)
bot = Bot(bot_token)
dp = Dispatcher(bot)
Tabnine | Edit | Test | Explain | Document | Ask
@dp.message_handler(commands=['start'])
async def start_handler(message: Itypes.Message):
first_name = message.from_user.first_name
await message.answer (f"Salom {first_name}\n\n\nBot @cypher_uzb tomonidan yoqildi!")
if_name_ == "_main__":
executor.start_polling(dp, skip_updates=True)
