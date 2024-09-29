import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7265109829:AAF-BVl4Z074U3A0eCeMkt5qH6lqqXhxemY")
    API_ID = int(os.environ.get("API_ID", "27500622")
    API_HASH = os.environ.get("API_HASH", "d45e39daf0e869ad0807311f14fb83fd")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "1002228957170")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = 'skip'
