import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5275758353:AAH8ZOacYu7n4dfXKXAYwLC4-0qzwK1Q7yU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
   await message.reply(f"Salom {message.chat.first_name}")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
