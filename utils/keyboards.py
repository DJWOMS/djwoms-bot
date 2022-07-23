from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton


def keyboard(
        menu_name: str = "menu_random",
        post_id: int = None,
        is_inline: bool = True,
        menu_rows: int = 4
):
    if is_inline:
        menu = InlineKeyboardMarkup()
    else:
        menu = ReplyKeyboardMarkup()

    menu.row_width = menu_rows
    menu.resize_keyboard = True

    random_user = InlineKeyboardButton('Другой юзер', callback_data=f'random_{post_id}')

    if menu_name == "menu_random":
        menu.add(random_user)
    return menu
