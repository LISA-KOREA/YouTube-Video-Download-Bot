from datetime import datetime
from pyrogram import Client, filters


@Client.on_message(filters.command("date"))
def date(client, message):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message.reply_text(f"The current date and time is: {current_date}")
  
