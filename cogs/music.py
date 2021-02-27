import discord
from discord.ext import commands
# import youtube_dl as ytdl


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(aliases=["p"], brief='plays a song', description='plays a song')
    async def play(self, ctx, url):
        pass
    
    @commands.command(aliases=["s"], brief='stops a running song', description='stops a running song')
    async def stop(self, ctx, song):
        pass

    @commands.command(aliases=["pa"], brief='pauses a running song', description='pauses a running song')
    async def pause(self, ctx, song):
        pass

    @commands.command(aliases=["r"], brief='resumes a stopped song', description='resumes a stopped song')
    async def resume(self):
        pass

    @commands.command(aliases=["q"], brief='dysplays the queue', description='dysplays the queue')
    async def queue(self):
        pass


def setup(client):
    client.add_cog(Music(client))
