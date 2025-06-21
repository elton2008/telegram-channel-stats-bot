from pyrogram import Client, filters
import asyncio

api_id = 23549032
api_hash = "ddfeafaf1e87a9662c9efc28e7b6d6ca"

app = Client("my_stats_session", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.private & filters.command("stats"))
async def stats_handler(client, message):
    if len(message.command) < 2:
        await message.reply("❌ Please provide a channel username.\nUsage: `/stats nasa`", parse_mode="markdown")
        return

    channel = message.command[1]
    if not channel.startswith("@"):
        channel = f"@{channel}"

    await message.reply(f"📊 Gathering stats for {channel}...\nThis may take a moment...")

    total_messages = 0
    total_views = 0
    total_reactions = 0

    try:
        async for msg in client.get_chat_history(channel):
            total_messages += 1
            total_views += msg.views or 0
            if msg.reactions and msg.reactions.reactions:
                for reaction in msg.reactions.reactions:
                    total_reactions += reaction.count
    except Exception as e:
        await message.reply(f"❌ Error: {e}")
        return

    await message.reply(
        f"📊 Channel Stats for {channel}:\n"
        f"📝 Messages: {total_messages}\n"
        f"👁️ Total Views: {total_views}\n"
        f"❤️ Total Reactions: {total_reactions}"
    )

print("🤖 Bot is running...")
app.run()

