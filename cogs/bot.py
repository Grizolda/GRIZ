import discord
from discord.ext import commands
from discord import Embed
from discord import __version__ as discord_version

from psutil import Process, virtual_memory, cpu_times
from platform import python_version

from datetime import datetime, timedelta
from time import time

VERSION = '0.0.1'
PREFIX = '&'


class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief='returns the bot latency', description='returns the bot latency')
    async def ping(self, ctx):
        await ctx.send(f"latency: {int(self.client.latency * 1000)} ms.")

    @commands.command(brief='returns the bot prefix', description='returns the bot prefix')
    async def prefix(self, ctx):
        await ctx.channel.send(f'my prefix is \'{PREFIX}\'.')

    @commands.command(brief='loads an extension', description='loads an extension')
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension.lower()}')
        print(f"extension '{extension}' loaded.")

    @commands.command(brief='unloads an extension', description='unloads an extension')
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension.lower()}')
        print(f"extension '{extension}' unloaded.")

    @commands.command(aliases=['binfo'], brief='returns the bot\'s info', description='returns the bot\'s info')
    async def botinfo(self, ctx):
        info = Embed(title='GRIZ info',
        description='The bot\'s info',
        colour=discord.Colour.purple(),
        thumbnail=self.client.user.avatar_url,
        timestamp=datetime.utcnow())

        proc = Process()
        with proc.oneshot():
            uptime = timedelta(seconds=time()-proc.create_time())
            cpu_time = timedelta(seconds=cpu_times().system + cpu_times().user)
            mem_total = virtual_memory().total / (1024**2)
            mem_of_total = proc.memory_percent()
            mem_usage = mem_total * (mem_of_total / 100)

        fields = [
            ('Bot version', VERSION, True),
            ('Python version', python_version(), True),
            ('discord.py version', discord_version, True),
            ('Uptime', uptime, True),
            ('CPU time', cpu_time, True),
            ('Memory usage', f'{mem_usage:,.3f} / {mem_total:,.0f} ({mem_of_total}%)', True),
            ('Guilds', f'used in {len(self.client.guilds)} servers', True),
        ]

        for name, value, inline in fields:
            info.add_field(name=name, value=value, inline=inline)

        await ctx.channel.send(embed=info)

        await ctx.send(embed=botinfo)

def setup(client):
    client.add_cog(Bot(client))
