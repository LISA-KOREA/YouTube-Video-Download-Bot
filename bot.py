# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL
import logging
#logging.basicConfig(level=logging.INFO)

from pyrogram import Client, filters
from pytube import YouTube
from pytube.exceptions import RegexMatchError, AgeRestrictedError
import asyncio

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

        # Download the YouTube video
        yt = YouTube(youtube_link)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if video:
            video.download(filename='downloaded_video.mp4')

            # Uploading text message
            uploading_msg = await message.reply_text("Uploading video...")

            # Send the video file to the user
            sent_message = await app.send_video(message.chat.id, video=open('downloaded_video.mp4', 'rb'), caption=yt.title)

            # Delay for a few seconds and delete downloading and uploading
            await asyncio.sleep(2)
            await downloading_msg.delete()
            await uploading_msg.delete()

            # Send successful upload message
            await message.reply_text("\n\nOWNER : @LISA_FAN_LK 💕\n\nSUCCESSFULLY UPLOADED!")
        else:
            logging.error("No video streams found.")
            await message.reply_text("Error: No downloadable video found.")
    except RegexMatchError:
        logging.error("Invalid YouTube link format.")
        await message.reply_text("Error: Invalid YouTube link format.")
    except AgeRestrictedError:
        logging.error("Age restricted video.")
        await message.reply_text("Error: The video is age restricted and cannot be downloaded.")
    except Exception as e:
        logging.exception("Error processing YouTube link: %s", e)
        await message.reply_text("Error: Failed to process the YouTube link. Please try again later.")

# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
