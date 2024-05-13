# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot

from pyrogram import Client, filters
import yt_dlp

# Define a command handler to generate thumbnail
@Client.on_message(filters.command("thumbnail"))
def generate_thumbnail(client, message):
    try:
        # Get the YouTube video URL from the message
        video_url = message.text.split(" ", 1)[1]

        wait_message = message.reply_text("Downloading your thumbnail")
        
        # Get the thumbnail URL using yt-dlp
        with yt_dlp.YoutubeDL({}) as ydl:
            info = ydl.extract_info(video_url, download=False)
            thumbnail_url = info.get('thumbnail')

        # Send the thumbnail URL back to the user
        message.reply_text(f"Thumbnail URL: {thumbnail_url}")
        
        wait_message.delete()
    
    except Exception as e:
        message.reply_text(f"Error: {str(e)}")
