#-*- coding: utf-8 -*-
import discord
from discord.ext import commands
from dataType.ListChained import ListChained
from discord import app_commands

import os

from constant import *


class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.historic = None
        self.registerCommand()
        self.registerSlashCommand()
        self.registerContextMenu()


        

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

        contentOfDir = os.listdir(COMMANDS_MESSAGE_DIR)
        for file in contentOfDir:
            if file.endswith(".py"):
                with open(COMMANDS_MESSAGE_DIR+"/"+file) as f:
                    env = {'client': self}
                    code = compile(f.read(), file, 'exec')
                    exec(code, env)


        # @self.command()
        # async def add(ctx,data):
        #     if self.historic == None:
        #         self.historic = ListChained(data)
        #     else:
        #         self.historic.append(data)
        #     await ctx.send(self.historic)

        # @self.command()
        # async def insert(ctx,indice,data):
        #     if self.historic == None:
        #         self.historic = ListChained(data)
        #     else:
        #         self.historic.insert(indice,data)
        #     await ctx.send(self.historic)

        # @self.command()
        # async def insert_first(ctx,data):
        #     if self.historic == None:
        #         self.historic = ListChained(data)
        #     else:
        #         self.historic.insert_first(data)
        #     await ctx.send(self.historic)        

        # @self.command()
        # async def ping(ctx):
        #     await ctx.send('Pong!')

        # @self.command()
        # async def delete(ctx, amount=5):
        #     await ctx.channel.purge(limit=amount)
    


    def registerSlashCommand(self):
        

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

        @self.tree.command()
        @app_commands.describe(name='The name of role to create')
        async def create_role(interaction: discord.Interaction, name: str):
            """Create a role"""
            guild = interaction.guild
            if discord.utils.get(guild.roles, name=name) is not None:
                return await interaction.response.send_message('That role already exists.', ephemeral=True)
            await guild.create_role(name=name)
            await interaction.response.send_message(f'Created the {name} role.', ephemeral=True)


        @self.tree.command()
        @app_commands.describe(name='The name of role to add')
        async def add_role(interaction: discord.Interaction, name: str):
            """Add a role to the user"""
            guild = interaction.guild
            role = discord.utils.get(guild.roles, name=name)
            if role is None:
                return await interaction.response.send_message('That role does not exist.', ephemeral=True)
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f'Added the {role.name} role to you.', ephemeral=True)

        @self.tree.command()
        @app_commands.describe(name='The name of role to remove')
        async def remove_role(interaction: discord.Interaction, name: str):
            """Remove a role from the user"""
            guild = interaction.guild
            role = discord.utils.get(guild.roles, name=name)
            if role is None:
                return await interaction.response.send_message('That role does not exist.', ephemeral=True)
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f'Removed the {role.name} role from you.', ephemeral=True)



    def registerContextMenu(self):
        @self.tree.context_menu(name="Turn Off")
        async def turnoff(interaction : discord.Interaction, user : discord.Member):
            if interaction.user.id != OWNER_ID:
                return await interaction.response.send_message('You are not the owner of this bot.', ephemeral=True)
            await interaction.response.send_message('Turning off...', ephemeral=True)
            await self.close()