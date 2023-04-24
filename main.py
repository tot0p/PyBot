#-*- coding: utf-8 -*-

import discord
from tools import env
from client import Client




def Init():
    """Initialize environment variables."""
    env.LoadEnv()
        


if __name__ == '__main__':
    Init()
    Intents = discord.Intents.all()
    client = Client(intents=Intents,command_prefix='!')
    client.run(env.Get('DISCORD_TOKEN'))

    
