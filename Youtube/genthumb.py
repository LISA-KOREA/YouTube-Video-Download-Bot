# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot
# ⚠️ Do not change this repo link ⚠️
# Repo: https://github.com/LISA-KOREA/YouTube-Video-Download-Bot

from pyrogram import Client, filters
import yt_dlp
import aiohttp
import os

@Client.on_message(filters.command("thumbnail"))
async def generate_thumbnail(client, message):
    if len(message.command) < 2:
        return await message.reply_text("❗Please provide a YouTube video link.\n\n**Example:** `/thumbnail <YouTube_URL>`")

    video_url = message.text.split(" ", 1)[1]
    wait = await message.reply_text("🔍 Fetching thumbnail...")

    try:
        # Extract video info without downloading
        with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(video_url, download=False)
            thumbnail_url = info.get("thumbnail")

        if not thumbnail_url:
            await wait.delete()
            return await message.reply_text("⚠️ Couldn’t find any thumbnail for this video.")

        # Try sending the actual image
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail_url) as resp:
                if resp.status == 200:
                    file_name = "thumb.jpg"
                    with open(file_name, "wb") as f:
                        f.write(await resp.read())

                    await message.reply_photo(photo=file_name, caption="🖼️ **Video Thumbnail**")
                    os.remove(file_name)
                else:
                    await message.reply_text(f"Thumbnail URL: {thumbnail_url}")

        await wait.delete()

    except Exception as e:
        await wait.delete()
        await message.reply_text(f"❌ Error: `{str(e)}`")
