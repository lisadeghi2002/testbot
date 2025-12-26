import asyncio
import random
import threading
from telethon import TelegramClient
from fastapi import FastAPI
import uvicorn
import os

API_ID = 34384738
API_HASH = "5ec5a6a4d89e2f50f76a9ce62300e19a"
GROUP_ID = -1003311162888

shoars = [
    "مرگ بر شاه",
    "جانم فدای رهبر",
    "ما بیداریم",
    "ما ملت امام حسینیم",
    "ما ملت شهادتیم"
]

client = TelegramClient("my_account", API_ID, API_HASH)

# -------- TELETHON PART --------
async def spammer():
    while True:
        await client.send_message(GROUP_ID, random.choice(shoars))
        await asyncio.sleep(random.randint(200, 250))

async def bot_main():
    await client.start()
    await spammer()

def start_bot():
    asyncio.run(bot_main())

# -------- WEB PART --------
app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

if __name__ == "__main__":
    # اجرای بات در ترد جدا
    threading.Thread(target=start_bot, daemon=True).start()

    # اجرای وب‌سرور (برای Render)
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
