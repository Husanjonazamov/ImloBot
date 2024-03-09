import logging
from Copital import get_capital
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6418058572:AAFYnF5cb9tZyqSUE3USsKHLO7TiybwUGCM'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply("Assalomu alaykum")


@dp.message_handler()
async def echo(message: types.Message):
    text = message.text()
    await message.reply(f"{get_capital(text)}")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)