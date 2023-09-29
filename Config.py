import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("20628949"))
    API_HASH = os.environ.get("9fd502d66505f2f6f8b6bf50e8a26b32")
    BOT_TOKEN = os.environ.get("6645400469:AAEiodfO1kO6IM904Kg0CeYTLyM2YlTu40w")
    BOT_USERNAME = os.environ.get("AhriV2_bot")
    BOT_NAME = os.environ.get("AhriV2")
    BOT_ID = int(os.environ.get("6645400469"))
    SUDO_USERS = os.environ.get("lexper").split()
    SUPPORT_CHAT = os.environ.get("redhackchet")
    OWNER_ID = int(os.environ.get("5944841427"))
    OWNER_USERNAME = os.environ.get("rahmetiNC")
