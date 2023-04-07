#-*- coding: utf-8 -*-
import discord
from discord.ext import commands
from dataType.ListChained import ListChained
from discord import app_commands

from constant import OWNER_ID


class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.historic = None
        self.registerCommand()

        

    async def on_ready(self):
        """Handle when the bot is ready"""
        print('We have logged in as {0.user}'.format(self))
        await self.tree.sync()
        await self.change_presence(activity=discord.Game(name="Hello World!"))

    async def on_message(self, message):
        """Handle messages sent to the bot"""
        if message.author == self.user:
            return
        
        message.content = message.content.lower()

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

        await super().process_commands(message)


    async def on_member_join(self, member):
        """Send a welcome message to the new member"""
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
        )

    async def close(self) -> None:
        return await super().close()
    
    async def clear(self) -> None:
        self._ready = False
        return await super().clear()
    
    def registerCommand(self):

        @self.command()
        async def add(ctx,data):
            if self.historic == None:
                self.historic = ListChained(data)
            else:
                self.historic.append(data)
            await ctx.send(self.historic)

        @self.command()
        async def insert(ctx,indice,data):
            if self.historic == None:
                self.historic = ListChained(data)
            else:
                self.historic.insert(indice,data)
            await ctx.send(self.historic)

        @self.command()
        async def insert_first(ctx,data):
            if self.historic == None:
                self.historic = ListChained(data)
            else:
                self.historic.insert_first(data)
            await ctx.send(self.historic)        

        @self.command()
        async def ping(ctx):
            await ctx.send('Pong!')

        @self.command()
        async def delete(ctx, amount=5):
            await ctx.channel.purge(limit=amount)
    
        @self.tree.command()
        @app_commands.describe(first='The first number to add', second='The second number to add')
        async def add(
            interaction: discord.Interaction,
            # This makes it so the first parameter can only be between 0 to 100.
            first: app_commands.Range[int, 0, 100],
            # This makes it so the second parameter must be over 0, with no maximum limit.
            second: app_commands.Range[int, 0, None],
        ):
            """Adds two numbers together"""
            await interaction.response.send_message(f'{first} + {second} = {first + second}', ephemeral=True)

        @self.tree.command()
        async def ping(interaction: discord.Interaction):
            """Pong!"""
            await interaction.response.send_message('Pong!', ephemeral=True)


        @self.tree.command()
        async def say(interaction: discord.Interaction, *, message: str):
            """Make the bot say something"""
            await interaction.response.send_message(message, ephemeral=True)

        @self.tree.command()
        async def turnoff(interaction: discord.Interaction):
            """Turn off the bot"""
            if interaction.user.id != OWNER_ID:
                return await interaction.response.send_message('You are not the owner of this bot.', ephemeral=True)
            await interaction.response.send_message('Turning off...', ephemeral=True)
            await self.close()

