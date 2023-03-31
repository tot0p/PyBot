#-*- coding: utf-8 -*-


import discord

from discord.ext import commands
from dataType.ListChained import ListChained


class Client(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.historic = ListChained(None)
        self.registerCommand()

    async def on_ready(self):
        """Handle when the bot is ready"""
        print('We have logged in as {0.user}'.format(self))
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
            self.historic.append(data)
            await ctx.send('Added!')
            await ctx.send("Historic: "+str(self.historic.size)+" elements")
            await ctx.send(self.historic)

        @self.command()
        async def ping(ctx):
            await ctx.send('Pong!')

        @self.command()
        async def delete(ctx, amount=5):
            await ctx.channel.purge(limit=amount)
    
    

