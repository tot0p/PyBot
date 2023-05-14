#-*- coding: utf-8 -*-

import discord


@client.tree.context_menu()
async def ping(interaction : discord.Interaction, user : discord.Member):
    await interaction.response.send_message('Pong!', ephemeral=True)