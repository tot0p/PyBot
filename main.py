#-*- coding: utf-8 -*-

import discord
from tools import env
from client import Client

import argparse



def Init():
    """Initialize environment variables."""
    env.LoadEnv()
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', type=str, help='Le token à utiliser')

    # Analyse des arguments de la ligne de commande
    args = parser.parse_args()
    if args.token:
        env.Set('DISCORD_TOKEN', args.token)



if __name__ == '__main__':
    Init()
    token = env.Get('DISCORD_TOKEN')
    if token is None:
        print('DISCORD_TOKEN is not set.')
        exit(1)
    Intents = discord.Intents.all()
    client = Client(intents=Intents,command_prefix='!')
    client.run(token)

    
