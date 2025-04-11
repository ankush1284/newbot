import motor.motor_asyncio
from config import Config

class Database:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(Config.DATABASE_URI)
        self.db = self.client[Config.DATABASE_NAME]
        self.users = self.db.users
        self.settings = self.db.settings

    async def init_user(self, user_id):
        await self.users.update_one(
            {"_id": user_id},
            {"$set": {
                "caption": "",
                "caption_enabled": True,
                "thumbnail": None,
                "replace_rules": [],
                "blacklist": []
            }},
            upsert=True
        )

db = Database()
