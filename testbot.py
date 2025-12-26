import os
from telethon import TelegramClient
import asyncio
import random

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
GROUP_ID = int(os.environ["GROUP_ID"])

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
