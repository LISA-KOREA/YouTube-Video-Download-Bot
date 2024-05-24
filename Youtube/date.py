from datetime import datetime
import pytz
from pyrogram import Client, filters

@Client.on_message(filters.command("date"))
def date(client, message):
    # Dictionary of time zones for various countries
    country_timezones = {
        "Argentina": 'America/Argentina/Buenos_Aires',
        "Australia Eastern": 'Australia/Sydney',
        "Australia Central": 'Australia/Adelaide',
        "Australia Western": 'Australia/Perth',
        "Brazil": 'America/Sao_Paulo',
        "Canada Eastern": 'America/Toronto',
        "Canada Central": 'America/Winnipeg',
        "Canada Mountain": 'America/Edmonton',
        "Canada Pacific": 'America/Vancouver',
        "China": 'Asia/Shanghai',
        "France": 'Europe/Paris',
        "Germany": 'Europe/Berlin',
        "India": 'Asia/Kolkata',
        "Japan": 'Asia/Tokyo',
        "Mexico": 'America/Mexico_City',
        "Russia Moscow": 'Europe/Moscow',
        "Russia Kamchatka": 'Asia/Kamchatka',
        "Saudi Arabia": 'Asia/Riyadh',
        "South Africa": 'Africa/Johannesburg',
        "South Korea": 'Asia/Seoul',
        "UAE": 'Asia/Dubai',
        "UK": 'Europe/London',
        "USA Eastern": 'America/New_York',
        "USA Central": 'America/Chicago',
        "USA Mountain": 'America/Denver',
        "USA Pacific": 'America/Los_Angeles',
        "USA Alaska": 'America/Anchorage',
        "USA Hawaii": 'Pacific/Honolulu'
    }

    # Get the country from the message text if provided
    country = "South Korea"  # Default to south korea
    if len(message.command) > 1:
        country = " ".join(message.command[1:])
    
    if country in country_timezones:
        timezone = pytz.timezone(country_timezones[country])
        current_date = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        message.reply_text(f"The current date and time in {country} is: {current_date}")
    else:
        message.reply_text("Sorry, I don't have the time zone information for that country.")
