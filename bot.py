# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL

import logging
import asyncio
import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
########################🎊 Lisa | NT BOTS 🎊######################################################
# Replace 'YOUR_API_ID', 'YOUR_API_HASH', and 'YOUR_BOT_TOKEN' with your actual values
API_ID = ''
API_HASH = ''
BOT_TOKEN = ''
# Skip Or add your proxy link
HTTP_PROXY = ''
youtube_dl_username = None  
youtube_dl_password = None  
########################🎊 Lisa | NT BOTS 🎊######################################################
# Create a Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


########################🎊 Lisa | NT BOTS 🎊#####################################################
START_TXT = '**Hello,** {}!\n\n**Send me the YouTube link of the video you want to upload**'
ABOUT_TXT = """
╭───────────⍟
├📛 **My Name** : [YouTube Video Uploader Bot](https://t.me/YouTubeUploaderOneBot)
├📢 **Framework** : [Pyrogram 2.0.106](https://docs.pyrogram.org/)
├💮 **Language** : [Python 3.12.3](https://www.python.org)
├👥 **Support Group** : [NT BOTS SUPPORT](https://t.me/NT_BOTS_SUPPORT)
├🥏 **Channel** : [NT BOT CHANNEL](https://t.me/NT_BOT_CHANNEL)
├⛲ **Source** : [Click](https://github.com/LISA-KOREA/YouTube-Video-Download-Bot)
├🎓 **Developer** : [LISA_FAN_LK](https://t.me/LISA_FAN_LK)
╰───────────────⍟
"""


########################🎊 Lisa | NT BOTS 🎊#####################################################
# Callback query handler
@app.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()

# About command handler
@app.on_message(filters.private & filters.command("about"))
async def about(client, message):
    await message.reply_text(ABOUT_TXT, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('⛔️ Close', callback_data='cancel')]
        ]
    ))


# Start command handler
@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    #user = message.from_user
    await message.reply_text(START_TXT.format(message.from_user.first_name), reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('📍 Update Channel', url='https://t.me/NT_BOT_CHANNEL'),
            ],
            [
                InlineKeyboardButton('👩‍💻 Developer', url='https://t.me/LISA_FAN_LK'),
                InlineKeyboardButton('👥 Support Group', url='https://t.me/NT_BOTS_SUPPORT'),
            ],
            [
                InlineKeyboardButton('⛔️ Close', callback_data='cancel')
            ]
        ]
    ))

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

        ydl_opts = {
            'outtmpl': 'downloaded_video_%(id)s.%(ext)s',
            'progress_hooks': [lambda d: print(d['status'])]
        }

        if HTTP_PROXY != "":
            ydl_opts['proxy'] = HTTP_PROXY
        if youtube_dl_username is not None:
            ydl_opts['username'] = youtube_dl_username
        if youtube_dl_password is not None:
            ydl_opts['password'] = youtube_dl_password

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_link, download=False)
            title = info_dict.get('title', None)

            if title:
                ydl.download([youtube_link])

                # Uploading text message
                uploading_msg = await message.reply_text("Uploading video...")

                # Send the video file to the user
                video_filename = f"downloaded_video_{info_dict['id']}.mp4"
                sent_message = await app.send_video(message.chat.id, video=open(video_filename, 'rb'), caption=title)


                # Delay for a few seconds and delete downloading and uploading
                await asyncio.sleep(2)
                await downloading_msg.delete()
                await uploading_msg.delete()

                # Send successful upload message
                await message.reply_text("\n\nOWNER : @LISA_FAN_LK 💕\n\nSUCCESSFULLY UPLOADED!")
            else:
                logging.error("No video streams found.")
                await message.reply_text("Error: No downloadable video found.")

    except Exception as e:
        logging.exception("Error processing YouTube link: %s", e)
        await message.reply_text("Error: Failed to process the YouTube link. Please try again later.")

# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
