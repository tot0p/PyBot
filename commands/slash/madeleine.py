#-*- coding: utf-8 -*-
import discord

@client.tree.command()
async def madeleine(interaction: discord.Interaction):
    """Pong!"""
    await interaction.response.send_message('https://tot0p.github.io/Lib/madeleineEmoji.png')