# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22179988"))
    API_HASH = getenv("API_HASH", "dae4b28e14b51583475a8def6ca06934)
    BOT_TOKEN = getenv("BOT_TOKEN", "7487183136:AAGvR-v27E5u2vQIUk4nxVytjqmGtUmtiH4")
    FSUB = getenv("FSUB", "loot_deals_hunter")
    CHID = int(getenv("CHID", "-1001907166812"))
    SUDO = list(map(int, getenv("SUDO", "1720819569").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://kefobi2259:RWxEMTIGj5Bc1Hz6@cluster0.bbn7aup.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
