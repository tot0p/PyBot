#-*- coding: utf-8 -*-
import discord

from discord import app_commands


@group.command(name='remove', description="Remove a role")
@app_commands.describe(name='The name of role to remove')
async def remove_role(interaction: discord.Interaction, name: str):
    """Remove a role"""
    guild = interaction.guild
    role = discord.utils.get(guild.roles, name=name)
    if role is None:
        return await interaction.response.send_message('That role does not exist.', ephemeral=True)
    await role.delete()
    await interaction.response.send_message(f'Removed the {name} role.', ephemeral=True)