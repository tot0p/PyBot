
import discord
from discord import app_commands

@group.command()
@app_commands.describe(name='The name of role to add')
async def add(interaction: discord.Interaction, name: str):
    """Add a role"""
    guild = interaction.guild
    role = discord.utils.get(guild.roles, name=name)
    if role is None:
        return await interaction.response.send_message('That role does not exist.', ephemeral=True)
    await interaction.user.add_roles(role)
    await interaction.response.send_message(f'Added the {role.name} role to you.', ephemeral=True)

