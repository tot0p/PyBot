import discord


@client.tree.context_menu(name="Turn Off")
async def turnoff(interaction : discord.Interaction, user : discord.Member):
    if interaction.user.id != OWNER_ID:
        return await interaction.response.send_message('You are not the owner of this bot.', ephemeral=True)
    

    client.historique.save()

    await interaction.response.send_message('Turning off...', ephemeral=True)
    await client.close()