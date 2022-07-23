from utils.core import *


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    if message.from_user.id in OWNERS:
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.full_name}', reply_markup=None)

@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await bot.send_message(message.from_user.id, f'Твой ID: <code>{message.from_user.id}</code>', reply_markup=None)
