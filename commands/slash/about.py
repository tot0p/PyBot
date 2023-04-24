#-*- coding: utf-8 -*-
import discord

import requests

@client.tree.command()
async def about(interaction: discord.Interaction):
    """About the bot!"""
    embed = discord.Embed(
        title = 'About',
        description = 'This bot is made by <@!{0}>'.format(OWNER_ID),
        color = 0x0000ff,
    )

    # get avatar github
    ownerInfo= requests.get("https://api.github.com/users/tot0p").json()    

    
    if "login" in ownerInfo and "html_url" in ownerInfo and "avatar_url" in ownerInfo :
        embed.set_author(name=ownerInfo["login"], url=ownerInfo["html_url"], icon_url=ownerInfo["avatar_url"])


    embed.add_field(name="Made with", value="discord.py", inline=True)
    embed.add_field(name="Github", value="[Here](https://github.com/tot0p/PyBot)", inline=True)
    embed.add_field(name="Invite", value="[Here](https://discord.com/oauth2/authorize?client_id=1091254412846051338&permissions=8&scope=bot)", inline=True)


    await interaction.response.send_message(embed=embed, ephemeral=False)
