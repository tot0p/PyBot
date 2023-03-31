#-*- coding: utf-8 -*-


import discord


class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
    

