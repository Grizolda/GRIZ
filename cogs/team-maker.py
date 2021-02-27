import discord
from discord.ext import commands


class TeamMaker(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(brief='returns a list of invited players to fill user\'s party',
     description='returns a list of invited players to fill user\'s party')
    async def fill(self, ctx, players, game):
        # get a list of players from the table named by the game name
        # random an amount of players from the table
        # send back a list of the players
        pass
    
    @commands.command(brief='adds a game to the query', description='adds a game to the query')
    async def game(self, game):
        # add a database table named by the game name
        pass
    
    @commands.command(brief='joins a user into the query', description='joins a user into the query')
    async def lobby(self, game):
        # insert the user name into the game table
        pass

def setup(client):
    client.add_cog(TeamMaker(client))
