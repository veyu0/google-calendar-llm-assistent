import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", "primary")
PORT = int(os.getenv("PORT", 8000))
PROXY_URL = os.getenv("PROXY_URL")