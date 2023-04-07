#-*- coding: utf-8 -*-
import discord

from discord import app_commands
import requests

@client.tree.command(description="Get github user info")
@app_commands.describe(user="Github user name")
async def github(interaction: discord.Interaction, user: str):
    """github user info"""
    userInfo = requests.get("https://api.github.com/users/"+user).json()
    if "name" not in userInfo:
        await interaction.response.send_message("User not found", ephemeral=True)
        return
    embed = discord.Embed(title=userInfo["name"], description=userInfo["bio"], color=0xeee657)
    embed.add_field(name="Public repos", value=userInfo["public_repos"], inline=True)
    embed.add_field(name="Followers", value=userInfo["followers"], inline=True)
    embed.add_field(name="Following", value=userInfo["following"], inline=True)
    embed.set_thumbnail(url=userInfo["avatar_url"])
    embed.set_author(name=userInfo["login"], url=userInfo["html_url"], icon_url=userInfo["avatar_url"])
    await interaction.response.send_message(embed=embed, ephemeral=False)