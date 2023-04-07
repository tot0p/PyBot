import discord

@group.command()
async def test(interaction: discord.Interaction):
    """Pong!"""
    await interaction.response.send_message('Pong!', ephemeral=True)