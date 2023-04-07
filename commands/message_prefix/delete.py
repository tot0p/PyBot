

@client.command()
async def delete(ctx, amount=5):
    await ctx.channel.purge(limit=amount)