#-*- coding: utf-8 -*-
import discord
from discord import app_commands

@group.command(name='channel', description="Send a message to a user")
@app_commands.describe(channel='The channel to send the message to')
@app_commands.describe(message='The message to send')
async def mp(interaction: discord.Interaction, channel : discord.TextChannel , message: str):
    """Send a message to a user"""
    # send the message
    await channel.send(message)
    await interaction.response.send_message(f'Sent the message to {channel.name}.', ephemeral=True)