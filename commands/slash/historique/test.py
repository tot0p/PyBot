#-*- coding: utf-8 -*-
import discord

from widget.pagination import PaginationView

@group.command(name='test', description="Show the historique")
async def test(interaction: discord.Interaction):
    """Show the historique"""
    embeds = [
        discord.Embed(title=f"Page {i}", description=f"This is page {i}") for i in range(1, 6)
    ]

    view = PaginationView(embeds)
    await interaction.response.send_message(embed=embeds[0], view=view)

