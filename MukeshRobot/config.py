
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "17763538" # integer value, dont use ""
    API_HASH = "babad31b4b434fc53d8bd13370c556c3"
    TOKEN = "6894743901:AAFlsaTrSwxaFpYMVXeXpkbr3NR_Nimoepw"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 6961211249 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "THE_FUCKER_BOTS_2926"  # Your own group for support, do not add the @
    START_IMG = "https://files.catbox.moe/jxk5hn.jpg"
    EVENT_LOGS = (-1002108743436)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://nakuldkdhacker:nakuldkdhacker$100@cluster0.45znzoj.mongodb.net/"
    # RECOMMENDED
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "9VTTT9B4QHV8DIDS"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "A8RZUCKYOVRS"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
