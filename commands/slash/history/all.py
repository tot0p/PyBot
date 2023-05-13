#-*- coding: utf-8 -*-
import discord


@group.command(name='show_all', description="Show all history")
async def show_all(interaction: discord.Interaction):
    """Show all history"""
    await interaction.response.send_message(client.historique.show(interaction.user.id), ephemeral=True)