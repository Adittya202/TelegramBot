from telethon import TelegramClient, events
import asyncio

api_id = 28326986
api_hash = '99cc9abb40fd8c1f2f8aef31da3965a5'
bot_token = '7765043505:AAFl_Z0jOoweJWZowe9XS0s89m7Fi_LMCAA'

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

async def send_message(message):
    await client.send_message('@colo_ssus007', message)

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    name = sender.username or sender.first_name or "someone"
    
    # Print the reply from the friend as soon as it arrives
    print(f"📥 Reply from {name}: {event.text}")

async def listen_for_input():
    while True:
        new_message = await asyncio.to_thread(input, "Enter message to send to bot: ")
        await send_message(new_message)

# Start the bot and the input listener
async def main():
    # Start bot message listening and also listen for terminal input at the same time
    await asyncio.gather(client.run_until_disconnected(), listen_for_input())

# Start the event loop manually
loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
