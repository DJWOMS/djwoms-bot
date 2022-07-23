from aiogram.utils import executor

from utils.core import dp
from utils.database import create_tables
from utils.h_commands import cmd_start
from utils.h_commands import cmd_id

from utils.h_inline import cb_inline_set_name
from utils.h_button import any_text


if __name__ == '__main__':
    create_tables()
    executor.start_polling(dp, skip_updates=True)
