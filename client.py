#-*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord import app_commands

from historique import Historique
import os
from constant import *


class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.historique = Historique()
        self.HelpAwTree = None # TODO : ADD AW TREE in HASHTABLE
        self.registerCommand()
        self.registerSlashCommand()
        self.registerContextMenu()


    async def on_ready(self):
        """Handle when the bot is ready"""
        print('We have logged in as {0.user}'.format(self))
        await self.tree.sync()
        await self.change_presence(activity=discord.Game(name="Hello World!"))

        # on all guilds, create channels
        # for guild in self.guilds:
        #     for channel in guild.channels:
        #         if channel.name == "general" or channel.name == "général":
        #             for member in guild.members:
        #                 await channel.send(member.mention)

        

    async def on_message(self, message):
        """Handle messages sent to the bot"""
        if message.author == self.user:
            return
        
        if message.author.bot:
            return
        

        if message.content == "hello":
            await message.channel.send("hello")
            return

        # message type mp
        if isinstance(message.channel, discord.channel.DMChannel):
            await message.channel.send("pas lu + ratio")
            return
        
        message.content = message.content.lower()

        self.historique.add(message.author.id,message.content)


        await super().process_commands(message)


    # events call for slash commands and context menu was called
    async def on_interaction(self, interaction):

        if interaction.type == discord.InteractionType.application_command and interaction.data["name"] != "historique":
            self.historique.add(interaction.user.id,"/"+interaction.data["name"])

        
    # async def on_typing(self, channel, user, when):
    #     """Handle when a user is typing in a channel"""
    #     await user.create_dm()
    #     await user.dm_channel.send(
    #         f'Hi {user.name}, you are typing in {channel.name}!'
    #     )

                



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
        load_commands(COMMANDS_MESSAGE_PREFIX_DIR,{"client":self,"OWNER_ID":OWNER_ID})
    
    def registerSlashCommand(self):
        load_slash_commands(COMMANDS_SLASH_DIR,{"client":self,"OWNER_ID":OWNER_ID})

    def registerContextMenu(self):
        load_commands(COMMANDS_CONTEXT_MENU_DIR,{"client":self,"OWNER_ID":OWNER_ID})
        

def load_commands(DIR: str,ENV : dict):
    contentOfDir = os.listdir(DIR)
    print("loading commands from "+DIR.replace("/"," "))
    for file in contentOfDir:
        if file.endswith(".py"):
            with open(DIR+"/"+file) as f:
                try:
                    code = compile(f.read(), file, 'exec')
                    exec(code, ENV)
                    print("loaded "+file[:-3])
                except Exception as e:
                    print("error while loading "+file)
                    print(e)
                    print("")

def load_slash_commands(DIR: str,ENV : dict):
    contentOfDir = os.listdir(DIR)
    print("loading commands from "+DIR.replace("/"," "))
    for file in contentOfDir:
        if file.endswith(".py"):
            with open(DIR+"/"+file) as f:
                try:
                    code = compile(f.read(), file, 'exec')
                    exec(code, ENV)
                    print("loaded "+file[:-3])
                except Exception as e:
                    print("error while loading "+file)
                    print(e)
                    print("")
        elif os.path.isdir(DIR+"/"+file) and file != "__pycache__" and file != "no_load":
            meta = {"description":"no description"}
            group = app_commands.Group(name=file,description=meta["description"])
            # add the group to the tree
            # load the commands in the group
            ENV["group"] = group
            load_slash_commands(DIR+"/"+file,ENV)
            ENV["client"].tree.add_command(group)
