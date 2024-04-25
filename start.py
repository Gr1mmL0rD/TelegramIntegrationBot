import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

string_token = "7149293032:AAHl2sNwAAv3cOzeAN9Jy7s7W6Ga0uPjftk"

dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

bot = Bot(string_token)


#Начало работы (/start)
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я буду уведомлять тебя о твоих заказах.")


#Просмотр пользователем всех своих заказов (/myOrders)
@dp.message(Command("myOrders"))
async def cmd_myOrders(message: types.Message):
    await message.answer("")

#Отчёт по средним оценкам сотрудников (/report)
@dp.message(Command("report"))
async def cmd_Report(message: types.Message):
    await message.answer("")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())