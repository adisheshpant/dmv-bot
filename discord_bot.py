import asyncio  
import discord
from dmv import checkDMV

client = discord.Client()
channel, task, delay = None, None, None
CLIENT_KEY = ""
CHANNEL_ID = ""

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

@client.event
async def on_message(message):
    global task, channel, client, delay
    content = message.content
    args = content.split(' ')
    print(content)

    if content.startswith('!delay'): 
        delay = int(args[1])

    elif content.startswith('!monitor'): 
        if not task: 
            print("Creating task")
            delay = int(args[1])
            task = client.loop.create_task(background_loop())
    
    elif content.startswith('!stop'): 
        if task:
            print("Stopping task")
            await client.send_message(channel, "Stopping monitor")
            task.cancel()
            task = None

async def background_loop():
    global channel, client, delay

    while not channel: 
        await client.wait_until_ready()
        channel = client.get_channel(CHANNEL_ID)
        if channel: break
        await asyncio.sleep(20)

    await client.send_message(channel, "Starting monitor")

    while not client.is_closed:
        result = checkDMV()
        print(result)
        if result[0]:
            await client.send_message(channel, "New slot available " + str(result[1]), tts = True) 
        await asyncio.sleep(delay)
        
client.run(CLIENT_KEY)
