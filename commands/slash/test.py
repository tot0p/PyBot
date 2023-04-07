
import discord

from widget.pagination import PaginationView

@client.tree.command()
async def paginate(interaction: discord.Interaction):
        data = [

        ]

        for i in range(1,15):
            data.append({
                "label": "User Event",
                "item": f"User {i} has been added"
            })

        pagination_view = PaginationView(timeout=None)
        pagination_view.data = data
        await pagination_view.send(interaction)