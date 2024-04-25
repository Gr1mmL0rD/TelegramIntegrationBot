import asyncio
import logging
import pyodbc
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from flask import Flask, request

string_token = "7149293032:AAHl2sNwAAv3cOzeAN9Jy7s7W6Ga0uPjftk"

conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=DESKTOP-NOO2N4A;DATABASE=PVZ_CHEMP;Trusted_Connection=yes;')

cursor = conn.cursor()

#query = "INSERT INTO dbo.Clients (ClientPhoneNumber, TelegramID) VALUES (?, ?)"
#values = ('message', 'user_id')
#cursor.execute(query, values)
conn.commit()
cursor.close()
conn.close()

dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

bot = Bot(string_token)


#Начало работы (/start)
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("""
Привет! Я буду уведомлять тебя о твоих заказах.
Для получения списка команд используйте /help
""")

#Регистрация (/reg)
@dp.message(Command("reg"))
async def cmd_reg(message: types.Message):
    await message.answer("Введите номер телефона для регистрации")
    conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=DESKTOP-NOO2N4A;DATABASE=PVZ_CHEMP;Trusted_Connection=yes;')
    cursor = conn.cursor()
    query = "INSERT INTO Clients (ClientPhoneNumber, TelegramID) VALUES (?, ?)"
    values = (message.text, message.chat.id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


#Просмотр пользователем всех своих заказов (/myOrders)
@dp.message(Command("myOrders"))
async def cmd_myOrders(message: types.Message):
    await message.answer("45555554")

#Отчёт по средним оценкам сотрудников (/report)
@dp.message(Command("report"))
async def cmd_report(message: types.Message):
    await message.answer("fsdf")

#Список всех команд бота (/help)
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("""
Список всех команд:
/reg      Регистрация
/myOrders Просмотр всех заказов
/report   Запрос отчёта по среним оценкам сотрудников
    """)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())