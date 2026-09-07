import os

import requests
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    response = requests.post(url, json=data, timeout=10)

    print(response.json())


send_message("🚨 Test: Minecraft bot работает!")