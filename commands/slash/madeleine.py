#-*- coding: utf-8 -*-
import discord

@client.tree.command()
async def madeleine(interaction: discord.Interaction):
    """Madeleine!"""
    await interaction.response.send_message('https://tot0p.github.io/Lib/madeleineEmoji.png')