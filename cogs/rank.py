import sqlite3 as sql
import discord
from discord.ext import commands


class Rank(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Rank(client))
