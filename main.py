from pyrogram import Client, filters, enums
from config import Config
from database import db
from plugins.captions import CaptionManager
from plugins.thumbnails import ThumbnailManager

app = Client(
    "forward_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

caption_mgr = CaptionManager()
thumb_mgr = ThumbnailManager()

@app.on_message(filters.command("start"))
async def start(client, message):
    # New interactive menu
    buttons = [
        [("⚙️ Settings", "settings")],
        [("📝 Captions", "caption_menu"), ("🖼️ Thumbnails", "thumb_menu")],
        [("🚀 Start Forwarding", "start_forward")]
    ]
    await message.reply(
        "**Advanced Forward Bot**\nChoose an option:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# [Rest of your forwarding logic...]
