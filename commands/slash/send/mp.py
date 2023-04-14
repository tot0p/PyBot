#-*- coding: utf-8 -*-
import discord
from discord import app_commands

@group.command(name='mp', description="Send a message to a user")
@app_commands.describe(user='The user to send the message to')
@app_commands.describe(message='The message to send')
async def mp(interaction: discord.Interaction, user: discord.Member , message: str):
    """Send a message to a user"""
    # send the message
    await user.create_dm()
    await user.dm_channel.send(message)

    await interaction.response.send_message(f'Sent the message to {user.name}.', ephemeral=True)

