#-*- coding: utf-8 -*-
import discord

@group.command(name='last', description="Show last command")
async def last(interaction: discord.Interaction):
    """Show last command"""
    await interaction.response.send_message(client.historique.last(interaction.user.id), ephemeral=True)