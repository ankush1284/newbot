from pyrogram import Client
from config import Config
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

async def run_bot():
    app = Client(
        "forward_bot",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="plugins")
    )
    
    await app.start()
    logging.info("Bot started successfully!")
    
    # Keep the bot running
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(run_bot())
