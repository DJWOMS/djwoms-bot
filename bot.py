from aiogram.utils import executor

from utils.core import dp
from utils.database import create_tables


if __name__ == '__main__':
    create_tables()
    executor.start_polling(dp, skip_updates=True)
