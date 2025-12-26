import asyncio
import random
from telethon import TelegramClient

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

async def spammer():
    while True:
        await client.send_message(GROUP_ID, random.choice(shoars))
        await asyncio.sleep(random.randint(200, 250))

async def main():
    await client.start()
    await spammer()

if __name__ == "__main__":
    asyncio.run(main())
