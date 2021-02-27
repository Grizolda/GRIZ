import discord
from discord.ext import commands
from discord import Embed

class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['report'], brief='sends a feedback\\report message to GRIZ team',
     description='sends a feedback\\report message to GRIZ team')
    async def feedback(self, ctx, report_message):
        pass

def setup(client):
    client.add_cog(Bot(client))
