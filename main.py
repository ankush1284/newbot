from pyrogram import Client
from config import Config
import asyncio

async def main():
    app = Client(
        "forward_bot",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="plugins")
    )
    
    await app.start()
    print("Bot is running...")
    
    # Keep the bot alive
    while True:
        await asyncio.sleep(3600)  # Sleep for 1 hour

if __name__ == "__main__":
    asyncio.run(main())
