from pyrogram import Client, filters
import os

# Take API details and token from environment variables
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Yo! Send me a channel username (without @) and I’ll show you its stats.")

@app.on_message(filters.text & ~filters.command("start"))
async def stats_handler(client, message):
    username = message.text.strip()
    try:
        total_messages = 0
        total_views = 0
        total_reactions = 0

        async for msg in app.get_chat_history(username):
            total_messages += 1
            total_views += msg.views or 0
            if msg.reactions and msg.reactions.reactions:
                for r in msg.reactions.reactions:
                    total_reactions += r.count

        await message.reply(
            f"📊 Stats for @{username}:\n"
            f"📝 Messages: {total_messages}\n"
            f"👁️ Views: {total_views}\n"
            f"❤️ Reactions: {total_reactions}"
        )
    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")

app.run()
