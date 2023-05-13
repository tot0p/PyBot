#-*- coding: utf-8 -*-
import discord

@group.command(name='clear', description="clear history")
async def clear(interaction: discord.Interaction):
    """Clear history"""
    await interaction.response.send_message(client.historique.clear(interaction.user.id), ephemeral=True)