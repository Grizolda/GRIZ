import discord
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # Commands
    
    @commands.command(brief='allowes member a permission', description='allowes member a permission')
    @commands.has_permissions(administrator=True)
    async def allow(self, ctx, member : discord.Member, permission):
        pass

def setup(client):
    client.add_cog(Server(client))
