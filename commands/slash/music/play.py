#-*- coding: utf-8 -*-
import discord

from discord import app_commands
import requests

@group.command(description="play youtube music")
@app_commands.describe(link='The link of the music to play')
async def play(interaction: discord.Interaction, link: str):
    
    await interaction.response.send_message(f'Playing {link}.', ephemeral=True)
