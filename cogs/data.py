import sqlite3 as sql
import os
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Cog

class Data(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @Cog.listener()
    async def on_guild_join(self, guild):
        # Create New Database For The Server
        if not f"./data/{guild.name}.db" in os.listdir():
            database = sql.connect(f"./data/{guild.name}.db")
            cursor = database.cursor()

            cursor.execute(f"CREATE TABLE IF NOT EXISTS members(member text, rank integer)")

            print(f"New connection found. created '{guild.name}' database.")
        
        perms = discord.Permissions()
        perms.update(send_messages = False)
        perms.update(connect = False)
        await guild.create_role(name="muted", permissions=perms)

    @Cog.listener()
    async def on_member_join(self, member):
        welcome_channel = self.client.get_channel(810867001849020456)
        await welcome_channel.send(f"> Hello {member.mention}, welcome to the server!")

        with sql.connect(f"./data/{member.guild.name}.db") as database:
            cursor = database.cursor()

            cursor.execute("INSERT INTO members VALUES (?, ?)", (member.name, 0))
    
    @Cog.listener()
    async def on_member_remove(self, member):
        with sql.connect(f"./data/{member.guild.name}.db") as database:
            cursor = database.cursor()

            members = cursor.execute("""SELECT member FROM members""")
            if member.name in members:
                cursor.execute(f"DELETE FROM members WHERE member={member.name}")
    
    @Cog.listener()
    async def on_message(self, message):
        '''with sql.connect(f"./data/{message.guild.name}.db") as database:
            cursor = database.cursor()

            members = cursor.execute("""SELECT member FROM members""").fetchall()
            member = message.author.name

            if member not in members:
                print(f"Member '{member}' not in '{message.guild.name} database.'")
                cursor.execute("""INSERT INTO members VALUES (?, ?)""", (member, 0))
                
        with sql.connect(f"./data/{message.guild.name}.db") as database:
            cursor = database.cursor()

            rank = cursor.execute(f"""SELECT rank FROM members WHERE member = {member}""")

            # updating the rank of the user by adding exprience
            cursor.execute(f"""UPDATE members SET rank = {rank + 1} WHERE member = {member}""")

        await message.channel.send(f"{message.author.name} is level {rank}")'''
        #await self.client.process_commands(message)
    
    @Cog.listener()
    async def on_guild_channel_create(self, channel):
        await channel.send("You may want to start setting up the channel. Start now?")
        await channel.send("> select a mode from the list below using `&set {mode}`.\n> This will set the channel to the mode selected.\
        \n> `team-maker    a mode wich includes a team-maker channel`")
        # Defining the channel mode

def setup(client):
    client.add_cog(Data(client))

