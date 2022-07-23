from utils.libs import *
from utils.variables import *
from utils.database import *

# logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
loop = asyncio.get_event_loop()
bot = Bot(token=API_TOKEN, loop=loop, parse_mode="html")
dp = Dispatcher(bot, loop=loop, storage=storage)
dp.middleware.setup(LoggingMiddleware())
