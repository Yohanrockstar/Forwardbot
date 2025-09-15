# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "1220805")
    API_HASH = environ.get("API_HASH", "b01d18cba6e1b7f206cc2d3d415ceed1")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5580538946:AAFKWNQfyL--YKq7utxi8ea1qNQgwXMke_s") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '865764383').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Yohanrock:yohanrockstar@cluster0.v8tewcp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002823015135'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
