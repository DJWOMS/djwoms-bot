from aiogram import types

from utils.core import dp, bot
from utils.database import Comment
from utils.keyboards import keyboard
from utils.variables import OWNERS


@dp.message_handler(content_types=types.ContentType.TEXT)
async def any_text(message: types.Message):
    if "reply_to_message" in message:
        post_id = message.reply_to_message.forward_from_message_id
        message_text = message.text if message.text else False
        if message_text:
            if message.from_user.is_bot is not True:
                comment = Comment(message=message)
                comment.add(post_id=post_id)

    if message.from_user.id in OWNERS:
        if "forward_from_message_id" in message:
            post_id = message.forward_from_message_id
            comment = Comment(message=message)
            get_text = comment.get_text(post_id=post_id)
            if get_text:
                await bot.send_message(
                    chat_id=message.from_user.id,
                    text=comment.get_text(post_id=post_id),
                    reply_markup=keyboard(post_id=post_id)
                )
            else:
                await bot.send_message(
                    chat_id=message.from_user.id,
                    text="Нет комментариев к этому посту",
                    reply_markup=None
                )
