import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6986631333:AAHJ1THDOYeWasJfJ58ARCmlyGcyCB2GPO8")
    API_ID = int(os.environ.get("API_ID", 4888076))
    API_HASH = os.environ.get("API_HASH", "8b9b8214d84305d5ba8042c93575ea84")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002040100311")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
