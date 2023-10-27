import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters.callback_data import CallbackData
from aiogram.filters.command import Command
from config_reader import bot_token
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=bot_token)

# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    username = message.from_user.username
    await message.answer("Привет {0}!".format(username))
    kb = [
        [
            types.KeyboardButton(text="Энергетиков"),
            types.KeyboardButton(text="Игримская"),
            types.KeyboardButton(text="с. Ярково")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выбери своё подазделение"
    )
    await message.answer("Ваше подразделение:", reply_markup=keyboard)

@dp.message(F.text.lower() == "Энергетиков")
async def with_puree(message: types.Message):
    await message.reply("Энергетиков файл", reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text.lower() == "Игримская")
async def without_puree(message: types.Message):
    await message.reply("Игримская файл")


@dp.message(F.text.lower() == "с. Ярково")
async def without_puree(message: types.Message):
    await message.reply("Ярково файл")






# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

