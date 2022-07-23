from utils.h_commands import *
from utils.h_inline import *
from utils.h_button import *


if __name__ == '__main__':
    create_tables()
    executor.start_polling(dp, skip_updates=True)
