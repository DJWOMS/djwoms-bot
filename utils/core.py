import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from utils.variables import API_TOKEN


storage = MemoryStorage()
loop = asyncio.get_event_loop()
bot = Bot(token=API_TOKEN, loop=loop, parse_mode="html")
dp = Dispatcher(bot, loop=loop, storage=storage)
dp.middleware.setup(LoggingMiddleware())
