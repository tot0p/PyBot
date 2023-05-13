#-*- coding: utf-8 -*-
import discord
from widget.pagination import PaginationView


@group.command(name='show', description="Show history")
async def show(interaction: discord.Interaction):
    """Show history"""
    txt = client.historique.show(interaction.user.id)
    embeds = []


    hist = txt.split('\n')
    hist.reverse()
    for i in range(0, len(hist), 10):
        embeds.append(discord.Embed(title=f"Page {i // 10 +1}", description='\n'.join(hist[i:i+10])))
    view = PaginationView(embeds)
    await interaction.response.send_message(embed=embeds[0], view=view)