#-*- coding: utf-8 -*-

import discord


@client.tree.command()
async def ecla(interaction: discord.Interaction):
    """ECLA"""
    
    embed = discord.Embed(title="ECLA", description="Ecla is a programming language that is designed to be easy to learn and use. It is a general purpose language that can be used for many different things.", color=0x54178a,url="https://github.com/Eclalang/Ecla")
    embed.add_field(name="Github", value="[Here](https://github.com/Eclalang/Ecla)", inline=True)
    embed.add_field(name="how to use", value="[Here](https://github.com/Eclalang/LearnEcla)", inline=True)

    embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/116202390?s=200&v=4")

    await interaction.response.send_message(embed=embed, ephemeral=False)

    
