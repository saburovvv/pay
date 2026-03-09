import asyncio
from telethon import TelegramClient, events
import requests

# Replace these with your own values
API_ID = 'your_api_id'
API_HASH = 'your_api_hash'
BOT_USERNAME = '@humocardbot'
WEBHOOK_URL = 'your_webhook_url'

# Create a new Telegram client
client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats=BOT_USERNAME))
async def handler(event):
    # Get the message text
    message_text = event.message.message
    
    # Extract numbers (modify this regex as needed)
    numbers = [int(s) for s in message_text.split() if s.isdigit()]
    
    # Send numbers to the webhook
    if numbers:
        requests.post(WEBHOOK_URL, json={'numbers': numbers})
        print(f'Sent numbers to webhook: {numbers}')

async def main():
    await client.start()
    print('Client is running...')
    await client.run_until_disconnected()

# Run the main function
asyncio.run(main())