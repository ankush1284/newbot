import os

class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    DATABASE_URI = os.getenv("DATABASE_URI")
    DATABASE_NAME = "forward_bot"
    MAX_FILE_SIZE = 2097152000  # 2GB
    BOT_OWNER = int(os.getenv("BOT_OWNER", 0))

class Temp:
    def __init__(self):
        self.user_tasks = {}
        self.locks = {}

temp = Temp()
