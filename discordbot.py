import discord
import os


intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

   
    if message.content.lower() == 'hello':
        await message.channel.send('world!')

    
    if message.content.startswith('!hello'):
        await message.channel.send('Hello there!')

# Fetch the bot token from environment variables
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if TOKEN:
    client.run(TOKEN)
else:
    print("Error: DISCORD_BOT_TOKEN not found.")
