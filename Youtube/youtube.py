# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot

import logging
import asyncio
import yt_dlp
from pyrogram import Client, filters
from Youtube.config import Config
from Youtube.forcesub import handle_force_subscribe


youtube_dl_username = None  
youtube_dl_password = None 

@Client.on_message(filters.regex(r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'))
async def process_youtube_link(client, message):
    if Config.CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    youtube_link = message.text
    try:
        downloading_msg = await message.reply_text("Downloading video...")

        ydl_opts = {
            'outtmpl': 'downloaded_video_%(id)s.%(ext)s',
            'progress_hooks': [lambda d: print(d['status'])]
        }

        if Config.HTTP_PROXY != "":
            ydl_opts['proxy'] = Config.HTTP_PROXY
        if youtube_dl_username is not None:
            ydl_opts['username'] = youtube_dl_username
        if youtube_dl_password is not None:
            ydl_opts['password'] = youtube_dl_password

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_link, download=False)
            title = info_dict.get('title', None)

            if title:
                ydl.download([youtube_link])
                uploading_msg = await message.reply_text("Uploading video...")
                video_filename = f"downloaded_video_{info_dict['id']}.mp4"
                sent_message = await client.send_video(message.chat.id, video=open(video_filename, 'rb'), caption=title)

                await asyncio.sleep(2)
                await downloading_msg.delete()
                await uploading_msg.delete()

                await message.reply_text("\n\nOWNER : @LISA_FAN_LK 💕\n\nSUCCESSFULLY UPLOADED!")
            else:
                logging.error("No video streams found.")
                await message.reply_text("Error: No downloadable video found.")
    except Exception as e:
        logging.exception("Error processing YouTube link: %s", e)
        await message.reply_text("Error: Failed to process the YouTube link. Please try again later.")
      
