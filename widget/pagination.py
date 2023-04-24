import discord


class PaginationView(discord.ui.View):
    def __init__(self, embeds):
        super().__init__(timeout=None)
        self.embeds = embeds
        self.current_embed = 0

    async def update_message(self, message):
        await message.edit(embed=self.embeds[self.current_embed], view=self)

    @discord.ui.button(label="<<", style=discord.ButtonStyle.blurple)
    async def first_page(self,  interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.current_embed = 0
        await self.update_message(interaction.message)

    @discord.ui.button(label="<", style=discord.ButtonStyle.blurple)
    async def previous_page(self,  interaction: discord.Interaction,button: discord.ui.Button):
        await interaction.response.defer()
        if self.current_embed > 0:
            self.current_embed -= 1
            await self.update_message(interaction.message)

    @discord.ui.button(label=">", style=discord.ButtonStyle.blurple)
    async def next_page(self,  interaction: discord.Interaction,button: discord.ui.Button):
        await interaction.response.defer()
        if self.current_embed < len(self.embeds) - 1:
            self.current_embed += 1
            await self.update_message(interaction.message)

    @discord.ui.button(label=">>", style=discord.ButtonStyle.blurple)
    async def last_page(self, interaction: discord.Interaction,button: discord.ui.Button):
        await interaction.response.defer()
        self.current_embed = len(self.embeds) - 1
        await self.update_message(interaction.message)

