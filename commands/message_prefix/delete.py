#-*- coding: utf-8 -*-

@client.command()
async def delete(ctx, amount=1):
    await ctx.channel.purge(limit=amount)