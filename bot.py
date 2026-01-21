# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.API_ID, '24424269'
    api_hash=Config.API_HASH, '6079d664c3117c18f353f21163fd1def'
    bot_token=Config.BOT_TOKEN,'8268220441:AAG1t4x0oer4BiZ4nG082NpDkmbjPqMDHYU'
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
