# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot

import os
import logging
import asyncio
import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Best Quality", callback_data=f"download|best|{youtube_link}")],
        [InlineKeyboardButton("1080p", callback_data=f"download|1080p|{youtube_link}")],
        [InlineKeyboardButton("2K", callback_data=f"download|2k|{youtube_link}")],
        [InlineKeyboardButton("4K", callback_data=f"download|4k|{youtube_link}")],
        [InlineKeyboardButton("Medium Quality", callback_data=f"download|medium|{youtube_link}")],
        [InlineKeyboardButton("Low Quality", callback_data=f"download|low|{youtube_link}")]
    ])
    
    await message.reply_text("Choose the video quality:", reply_markup=keyboard)

@Client.on_callback_query(filters.regex(r'^download\|'))
async def handle_download_button(client, callback_query):
    quality, youtube_link = callback_query.data.split('|')[1:]
    
    quality_format = {
        'best': 'best',
        '1080p': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        '2k': 'bestvideo[height<=1440]+bestaudio/best[height<=1440]',
        '4k': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
        'medium': 'best[height<=480]',
        'low': 'best[height<=360]'
    }.get(quality, 'best')

    try:
        downloading_msg = await callback_query.message.reply_text("Downloading video...")

        ydl_opts = {
            'format': quality_format,
            'outtmpl': 'downloaded_video_%(id)s.%(ext)s',
            'progress_hooks': [lambda d: print(d['status'])],
            'cookiefile': 'cookies.txt'
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
                uploading_msg = await callback_query.message.reply_text("Uploading video...")
                video_filename = f"downloaded_video_{info_dict['id']}.mp4"
                sent_message = await client.send_video(callback_query.message.chat.id, video=open(video_filename, 'rb'), caption=title)

                await asyncio.sleep(2)
                await downloading_msg.delete()
                await uploading_msg.delete()

                await callback_query.message.reply_text("\n\nOWNER : @LISA_FAN_LK 💕\n\nSUCCESSFULLY UPLOADED!")
            else:
                logging.error("No video streams found.")
                await callback_query.message.reply_text("Error: No downloadable video found.")
    except Exception as e:
        logging.exception("Error processing YouTube link: %s", e)
        await callback_query.message.reply_text("Error: Failed to process the YouTube link. Please try again later.")
