from utils.libs import *


def settings():
    with open("./config.json", "r", encoding="utf-8") as f:
        return dict(json.loads(f.read()))


CFG = settings()

API_TOKEN = CFG.get("api_token", None)

OWNERS = CFG.get("owners", None)
DB_NAME = CFG.get("db_name", None)

LANGS = CFG.get("langs", None)
