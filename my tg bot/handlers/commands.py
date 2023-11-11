# handlers/commands.py
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from ..main import dp


@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Это бот.")