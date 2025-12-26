import os
from telethon import TelegramClient
import asyncio
import random

API_ID = 34384738
API_HASH = "5ec5a6a4d89e2f50f76a9ce62300e19a"
GROUP_ID = -1003311162888

session_name = "my_account"

shoars = [
    "مرگ بر شاه",
    "جانم فدای رهبر",
    "ما بیداریم",
    "ما ملت امام حسینیم",
    "ما ملت شهادتیم"
]

client = TelegramClient(session_name, API_ID, API_HASH)

async def spammer():
    while True:
        delay = random.randint(200, 250)
        await client.send_message(
            GROUP_ID,
            random.choice(shoars)
        )
        await asyncio.sleep(delay)

async def main():
    await client.start()
    await spammer()

with client:
    client.loop.run_until_complete(main())
