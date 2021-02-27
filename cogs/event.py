import discord
from discord.ext import commands, tasks


class Event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief='sets a new event', description='sets a new event')
    @commands.has_permissions(administrator=True)
    async def event(self, ctx, event_time, *, event_text):
        pass #inserting a new event into the database
    
    async def send_event(self, ctx, event):
        pass
    

    '''@tasks.loop()
    # checking for events'''

def setup(client):
    client.add_cog(Event(client))
