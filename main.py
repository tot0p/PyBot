#-*- coding: utf-8 -*-

import discord
from tools import env
from client import Client

import time



def Init():
    """Initialize environment variables."""
    env.LoadEnv()
        

if __name__ == '__main__':
    Init()
    Intents = discord.Intents.all()
    client = Client(intents=Intents,command_prefix='!')

    # @client.command()
    # async def ping(ctx):
    #     await ctx.send('Pong!')

    client.run(env.Get('DISCORD_TOKEN'))
