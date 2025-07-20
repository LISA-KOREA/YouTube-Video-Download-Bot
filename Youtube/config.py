import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("7986939659:AAEek57A-2tF1MRLnmZ0B76tJrHOIv2twQo", "")
    API_ID = int(os.environ.get("19241729", ))
    API_HASH = os.environ.get("f96f8c309ac68bc8d7c39adbbfec6000", "")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
