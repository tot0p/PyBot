#-*- coding: utf-8 -*-
import discord

@group.command(name='last', description="Show the historique")
async def last(interaction: discord.Interaction):
    """Show the historique"""
    await interaction.response.send_message(client.historique.last(interaction.user.id), ephemeral=True)