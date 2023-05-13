#-*- coding: utf-8 -*-


# repository of api : https://github.com/tot0p/joke (made by me)
# api url : https://tot0p.github.io/joke/api/joke/random/lang/{lang}/ change {lang} by fr )

import discord
from discord import app_commands


import enum
import requests

class Lang(enum.Enum):
    fr = 'fr'
    en = 'en'


@client.tree.command(description="Get a joke")
@app_commands.describe(lang='The language of the joke')
async def joke(interaction: discord.Interaction,lang : Lang = Lang.fr):
    """get a joke"""
    rep = requests.get(f"https://tot0p.github.io/joke/api/joke/random/lang/{lang.value}/").json()
    if "title" not in rep or "content" not in rep:
        await interaction.response.send_message("Error", ephemeral=True)
        return
    
    print(rep)
    embed = discord.Embed(title=rep["title"], color=0xeee657,description=rep["content"])
    await interaction.response.send_message(embed=embed, ephemeral=False)