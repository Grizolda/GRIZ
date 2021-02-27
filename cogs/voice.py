import discord
from discord.ext import commands


class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief='joins the bot to a channel', description='joins the bot to a channel')
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"joined channel '{channel}'.")
    
    @commands.command(brief='leave the bot from a channel', description='leave the bot from a channel')
    async def leave(self, ctx):
        channel = ctx.author.voice.channel
        await ctx.message.guild.voice_client.disconnect()
        await ctx.send(f"left channel '{channel}'.")
    
    @join.error
    @leave.error
    async def channel_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You must join a voice channel to use this command.")

def setup(client):
    client.add_cog(Voice(client))
