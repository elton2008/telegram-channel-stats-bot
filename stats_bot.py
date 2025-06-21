import os
from pyrogram import Client, filters
from pyrogram.types import Message

# Read sensitive info from environment variables
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply("👋 Hello! Send me a channel username to get its stats.")

app.run()
