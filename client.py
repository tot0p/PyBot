#-*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord import app_commands

from historique import Historique
import os
from config import *

import copy

from reco import LoadAwTreeHashTable

class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.historique = Historique()
        self.HelpAwTree = LoadAwTreeHashTable()
        self.AwTreeState = {}
        self.registerCommand()
        self.registerSlashCommand()
        self.registerContextMenu()

    def AddUserInAwTree(self,user_id,theme=""):
        self.AwTreeState[str(user_id)] = theme

    async def on_ready(self):
        """Handle when the bot is ready"""
        print('We have logged in as {0.user}'.format(self))
        await self.tree.sync()
        await self.change_presence(activity=discord.Game(name="Welcome to the jungle"))

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
        

        # message type mp
        if isinstance(message.channel, discord.channel.DMChannel):
            # send message of the user on the general channel
            for guild in self.guilds:
                if message.author in guild.members:
                    for channel in guild.channels:
                        if channel.name == "general" or channel.name == "général"  :
                            embed = discord.Embed(title="Message privé", description="Message privé de " + message.author.mention,color=0x0000FF)
                            embed.add_field(name="Message", value=message.content, inline=False)
                            embed.set_author(name=message.author.name, icon_url=message.author.avatar)
                            await channel.send(embed=embed)
            return
        
        message.content = message.content.lower()

        

        if not message.content.startswith("!") and str(message.author.id) in self.AwTreeState:
            if message.content == "reset":
                self.AwTreeState[str(message.author.id)] = ""
                await message.channel.send('What you want to talk about? (ex: "programming")')
                return 
            if "speak about" in message.content:
                message.content = message.content.split("speak about")[1].replace(" ","",1)
                if message.content in self.HelpAwTree.keys():
                    await message.channel.send("yes i can speak about "+message.content)
                else:
                    await message.channel.send("i don't know this theme")
                return
            elif self.AwTreeState[str(message.author.id)] == "":
                theme = self.HelpAwTree.get_value(message.content)
                if theme != None:
                    self.AwTreeState[str(message.author.id)] = copy.deepcopy(theme)
                    await message.channel.send(self.AwTreeState[str(message.author.id)].get_question())
                    return
                else:
                    await message.channel.send("i don't know this theme")
                    return
            else:
                if self.AwTreeState[str(message.author.id)].send_answer(message.content):
                    await message.channel.send(self.AwTreeState[str(message.author.id)].get_question())
                    if self.AwTreeState[str(message.author.id)].is_end():
                        del self.AwTreeState[str(message.author.id)]
                        await message.channel.send("if you want to restart the conversation, type !recommendation")
                    return
                else:
                    await message.channel.send("i don't know this answer")
                    return





        await super().process_commands(message)


    async def on_command(self, ctx):
        """Handle when a command is called"""
        #print(ctx.author.name + " called " + ctx.command.name + " with args " + str(ctx.args))
        self.historique.add(ctx.author.id, ctx.message.content)



    async def on_command_error(self, ctx, error):
        """Handle errors from commands"""
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Commande inconnue")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Argument manquant")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("Vous n'avez pas les permissions pour faire cette commande")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("Le bot n'a pas les permissions pour faire cette commande")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Cette commande est en cooldown, veuillez réessayer dans " + str(round(error.retry_after,2)) + " secondes")
        else:
            print(error)
            await ctx.send("Une erreur est survenue")

        

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
        elif os.path.isdir(DIR+"/"+file) and file != "__pycache__":
            meta = {"description":"no description"}
            group = app_commands.Group(name=file,description=meta["description"])
            # add the group to the tree
            # load the commands in the group
            ENV["group"] = group
            load_slash_commands(DIR+"/"+file,ENV)
            ENV["client"].tree.add_command(group)