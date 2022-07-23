from aiogram import types, utils

from utils.core import dp, bot
from utils.database import Comment
from utils.keyboards import keyboard


@dp.callback_query_handler(lambda c: str(c.data).startswith('random_'))
async def cb_inline_set_name(message: types.CallbackQuery):
    post_id = message.data[7:]
    comment = Comment(message=message)
    try:
        await bot.edit_message_text(
            comment.get_text(post_id=post_id),
            message.from_user.id,
            message.message.message_id,
            reply_markup=keyboard(post_id=post_id)
        )
    except utils.exceptions.MessageNotModified:
        pass
