import os
import requests
import time
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=TOKEN)

def get_proxy():
    try:
        res = requests.get("https://mtpro.xyz/api/").json()
        for p in res:
            return f"""🔰 پروکسی رایگان – 🇦🇺 {p['country']}
📶 اتصال پرسرعت مخصوص تلگرام  
📌 برند: FixProVPN  
🔗 {p['link']}"""
    except:
        return None

if name == "main":
    while True:
        msg = get_proxy()
        if msg:
            bot.send_message(chat_id=CHANNEL_ID, text=msg)
        time.sleep(3600)
