import asyncio
from telethon import TelegramClient, events
import requests
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sizning API ma'lumotlaringiz
API_ID = 24145128
API_HASH = '190a388c10ffadaf8a31fc0e8a9b9470'
BOT_USERNAME = 'humocardbot'
WEBHOOK_URL = 'https://pay-qb6n.onrender.com/webhook'

client = TelegramClient('session_name', API_ID, API_HASH)

def extract_numbers(text):
    """Matndan raqamlarni ajratib oladi"""
    return re.findall(r'\d+(?:\.\d+)?', text)

@client.on(events.NewMessage(from_users=BOT_USERNAME))
async def handler(event):
    text = event.raw_text
    sender = await event.get_sender()
    
    logger.info(f"📨 Xabar keldi: @{sender.username}")
    
    numbers = extract_numbers(text)
    
    if numbers:
        payload = {
            "numbers": numbers,
            "message": text,
            "sender_id": event.sender_id
        }
        
        try:
            response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
            logger.info(f"✅ Webhook: {response.status_code}")
        except Exception as e:
            logger.error(f"❌ Xatolik: {e}")

async def main():
    await client.start()
    logger.info("✅ Telegram akkauntga ulanildi!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
