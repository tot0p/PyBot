import discord

@group.command()
async def test2(interaction: discord.Interaction):
    """Pong!"""
    await interaction.response.send_message('Pong!', ephemeral=True)