#-*- coding: utf-8 -*-
import discord

from discord import app_commands

@group.command(name='create', description="Create a role")
@app_commands.describe(name='The name of role to create')
async def create_role(interaction: discord.Interaction, name: str):
    """Create a role"""
    guild = interaction.guild
    if discord.utils.get(guild.roles, name=name) is not None:
        return await interaction.response.send_message('That role already exists.', ephemeral=True)
    await guild.create_role(name=name)
    await interaction.response.send_message(f'Created the {name} role.', ephemeral=True)
