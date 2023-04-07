import discord

@client.tree.command()
async def ping(interaction: discord.Interaction):
    """Pong!"""
    await interaction.response.send_message('Pong!', ephemeral=True)