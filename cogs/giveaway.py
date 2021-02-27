import discord
from discord.ext import commands
import random


class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['gva'], brief='randoms a member from a role', description='randoms a member from a role')
    async def giveaway(self, ctx, role: discord.Role):
        if role not in ctx.message.server.roles:
            return await ctx.channel.send(f"no role '{role}' found.")
        
        for member in ctx.message.server.members:
            pass
    

def setup(client):
    client.add_cog(Giveaway(client))
