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
        load_commands(COMMANDS_MESSAGE_PREFIX_DIR,{"client":self,"OWNER_ID":OWNER_ID})
    
    def registerSlashCommand(self):
        load_commands(COMMANDS_SLASH_DIR,{"client":self,"OWNER_ID":OWNER_ID})

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