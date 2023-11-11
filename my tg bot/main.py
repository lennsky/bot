# main.py
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

from handlers import dp
from config import TOKEN

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp.middleware.setup(LoggingMiddleware())
dp.bot = bot

if __name__ == '__main__':
    from aiogram import executor
    from handlers.commands import dp

    executor.start_polling(dp, skip_updates=True)