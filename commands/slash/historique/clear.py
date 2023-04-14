#-*- coding: utf-8 -*-
import discord

@group.command(name='clear', description="clear the historique")
async def clear(interaction: discord.Interaction):
    """Show the historique"""
    await interaction.response.send_message(client.historique.clear(interaction.user.id), ephemeral=True)