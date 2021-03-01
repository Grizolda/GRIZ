import os
import sqlite3 as sql

import discord
from discord import Intents, Embed
from discord.ext import commands

intents = Intents.default()
intents.members = True
intents.presences = False
#intents.presence = True

VERSION = '0.0.1'
PREFIX = '&'
TOKEN = "ODEyNzUwODAzNDY2MDU5ODA2.YDFTKw.FOpCJ0WesEyJ8hDjthNB2d2Oxxk"
client = commands.Bot(command_prefix=PREFIX, intents=intents)
client_id = 812750803466059806

# Bot events
@client.event
async def on_ready():
    print("Bot is online.\n\n")
    channel1 = client.get_channel(811883115718115358)
    channel2 = client.get_channel(814107482356056064)
    '''channels = {
        'channel1': 811883115718115358,
        'channel2': 814107482356056064
    }'''

    message = Embed(title='i\'m online!',
    description=f'GRIZ is ready! (latency: {int(client.latency * 1000)})',
    colour=discord.Colour.purple())

    '''for channel in channels:
        client.get_channel(channel.key)'''
    await channel1.send(embed=message)
    await channel2.send(embed=message)

    print(f"logged in as {client.user.name}.")
    print_bot_status()

@client.event
async def on_connect():
    print(f"Connected to Discord (latency: {int(client.latency * 1000)} ms).")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return # Ignoring unknown commands
    else:
        #await ctx.channel.send('an error occurred!')
        raise error

@client.event
async def on_message(message):
    if client.user in message.mentions:
        await message.channel.send('how can i help you?')
    
    await client.process_commands(message)

def connect_dbs():
    for filename in  os.listdir("./data/"):
        if filename.endswith('.db'):
            sql.connect(f"./data/{filename}")
    
    print("All databases are connected.")



def print_bot_status():
    print(f'Version: {VERSION}')

    guilds = [guild.name for guild in client.guilds]
    print(f"Guilds: {guilds}")

def setup_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') or filename.endswith('.js'):
            client.load_extension(f'cogs.{filename[:-3]}')

    print("cogs are ready.")

connect_dbs()
setup_cogs()
client.run(TOKEN, reconnect=True)
