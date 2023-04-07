#-*- coding: utf-8 -*-
import discord

@group.command(name='show', description="Show the historique")
async def show(interaction: discord.Interaction):
    """Show the historique"""
    await interaction.response.send_message(client.historique, ephemeral=True)