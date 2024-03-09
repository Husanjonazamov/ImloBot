import logging
from CheckWord import CheckWords
from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_latin, to_cyrillic


API_TOKEN = '6363333886:AAEfd8p1JesDMvvsZBzP8flwc-oNDihXFt4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply(f"<b>👋 Assalomu alaykum {message.from_user.first_name}!\n"
                        f"🤖 @UzBeimlobot botiga xush kelibsiz\n"
                        f"✅ Botdan qanday foydalanishni bilish uchun\n"
                        f"🚀 /help buyrug'ini yuboring</b>", parse_mode='HTML')

@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.reply("<b>🚀 Botga IMlosida qiynalayotgan so'zingizni yuboring\n"
                        "👌 va bir nechta misollar bilan qabul qiling</b>", parse_mode='HTML')

@dp.message_handler()
async def CheckImlo(message: types.Message):
    word = message.text
    result = CheckWords(to_cyrillic(word)) if word.isascii() else to_latin(word)
    if result['available']:
        response = f"✅ {to_latin(word.capitalize())}\n"
    else:
        response = f"❌ {to_latin(word.capitalize())}\n"
        for text in result['matches']:
            response += f"✅ {to_latin(text.capitalize())}\n"
    await message.reply(response)



@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)