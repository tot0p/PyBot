#-*- coding: utf-8 -*-

@client.command()
async def recommendation(ctx):
    if str(ctx.author.id) in client.AwTreeState:
        await ctx.send('You are already in the tree!')
        return
    client.AddUserInAwTree(ctx.author.id)
    await ctx.send('What you want to talk about? (ex: "programming")')