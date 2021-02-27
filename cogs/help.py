import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    '''@commands.command(brief='show\'s this message', description='show\'s a help message')
    async def help(self, ctx, role: discord.Role):
        pass'''
    

def setup(client):
    client.add_cog(Help(client))
