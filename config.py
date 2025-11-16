# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "24966518"))
API_HASH = getenv("API_HASH", "3c9081dac5ff9111f789939b67bc5f89")
BOT_TOKEN = getenv("BOT_TOKEN", "8596937720:AAHRrB3wASt7Oq55YW5WvMyVr5cVzqapmAI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8252171298").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002511726148"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", ""))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", ""))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "3c9081dac5ff9111f789939b67bc5f89")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
