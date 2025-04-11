from database import db
from pyrogram.types import InputMediaPhoto

class ThumbnailManager:
    async def set_thumbnail(self, user_id, file_id):
        await db.users.update_one(
            {"_id": user_id},
            {"$set": {"thumbnail": file_id}},
            upsert=True
        )

    async def get_thumbnail(self, user_id):
        user = await db.users.find_one({"_id": user_id})
        return user.get("thumbnail") if user else None

    async def enforce_thumbnail(self, message, user_id):
        thumb = await self.get_thumbnail(user_id)
        if not thumb:
            await message.reply("❌ You must set a thumbnail first with /setthumb")
            return False
        return thumb
