# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL
from pyrogram import Client, filters
import asyncio
import os
import youtube_dl

# Replace 'YOUR_API_ID', 'YOUR_API_HASH', and 'YOUR_BOT_TOKEN' with your actual values

API_ID = ''
API_HASH = ''
BOT_TOKEN = ''

# Create a Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start command handler
@app.on_message(filters.command("start"))
def start(client, message):
    user = message.from_user
    message.reply_text(f"Hello, @{user.username}!\n\nSend me the YouTube link of the video you want to upload.")

# Help command handler
@app.on_message(filters.command("help"))
def help(client, message):
    help_text = """
    Welcome to the YouTube Video Uploader Bot!

To upload a YouTube video, simply send me the YouTube link.
    
Enjoy using the bot!

   ©️ Channel : @NT_BOT_CHANNEL
    """
    message.reply_text(help_text)

# Message handler for processing YouTube links
@app.on_message(filters.regex(r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'))
async def process_youtube_link(client, message):
    youtube_link = message.text
    try:
        # Downloading text message
        downloading_msg = await message.reply_text("Downloading video...")

        # Download the YouTube video using youtube_dl
        ydl_opts = {'outtmpl': 'downloaded_video.mp4'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_link])

        # Uploading text message
        uploading_msg = await message.reply_text("Uploading video...")

        # Send the video file to the user
        await app.send_video(message.chat.id, video=open('downloaded_video.mp4', 'rb'), caption=ydl.extract_info(youtube_link, download=False).get('title'))

        # Clean up downloaded video file
        os.remove('downloaded_video.mp4')

        # Send successful upload message
        await message.reply_text("\n\nOWNER : @LISA_FAN_LK 💕\n\nSUCCESSFULLY UPLOADED!")

    except Exception as e:
        error_text = 'Error: Failed to process the YouTube link. Please make sure the link is valid and try again.'
        await message.reply_text(error_text)

# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
