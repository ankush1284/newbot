from database import db

class CaptionManager:
    async def add_text(self, user_id, text):
        await db.users.update_one(
            {"_id": user_id},
            {"$set": {"caption": f"{await self.get_caption(user_id)}{text}"}}
        )

    async def replace_text(self, user_id, old, new):
        current = await self.get_caption(user_id)
        await db.users.update_one(
            {"_id": user_id},
            {"$set": {"caption": current.replace(old, new)}}
        )

    async def delete_text(self, user_id, text):
        current = await self.get_caption(user_id)
        await db.users.update_one(
            {"_id": user_id},
            {"$set": {"caption": current.replace(text, "")}}
        )

    async def get_caption(self, user_id):
        user = await db.users.find_one({"_id": user_id})
        return user.get("caption", "") if user else ""

    async def toggle(self, user_id, status):
        await db.users.update_one(
            {"_id": user_id},
            {"$set": {"caption_enabled": status}}
        )
