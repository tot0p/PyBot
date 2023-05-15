#-*- coding: utf-8 -*-
import discord

from discord import app_commands
import requests

@client.tree.command(description="Get the most starred repo of a user")
@app_commands.describe(user="Github user name")
@app_commands.describe(with_orga="Include organizations")
async def best_repo(interaction: discord.Interaction, user: str = "tot0p", with_orga: bool = True):
    """github user info or tot0p if no user is specified"""
    repos = requests.get("https://api.github.com/users/"+user+"/repos").json()

    if "message" in repos:
        await interaction.response.send_message(repos["message"], ephemeral=True)
        return

    if len(repos) == 0:
        await interaction.response.send_message("User not found", ephemeral=True)
        return
    
    bestRepo = repos[0]
    for repo in repos:
        if repo["stargazers_count"] > bestRepo["stargazers_count"]:
            bestRepo = repo

    # get best repo in organizations
    if with_orga:
        orgs = requests.get("https://api.github.com/users/"+user+"/orgs").json()
        if "message" in orgs:
            await interaction.response.send_message(orgs["message"], ephemeral=True)
            return
        for org in orgs:
            orgRepos = requests.get("https://api.github.com/orgs/"+org["login"]+"/repos").json()
            if "message" in orgRepos:
                await interaction.response.send_message(orgRepos["message"], ephemeral=True)
                return
            for repo in orgRepos:
                if repo["stargazers_count"] > bestRepo["stargazers_count"]:
                    bestRepo = repo

    embed = discord.Embed(title=bestRepo["name"], description=bestRepo["description"], color=0x0000FF,url=bestRepo["html_url"])
    embed.add_field(name="Language", value=bestRepo["language"], inline=True)
    embed.add_field(name="Stars", value=bestRepo["stargazers_count"], inline=True)
    embed.add_field(name="Forks", value=bestRepo["forks_count"], inline=True)
    embed.set_author(name=bestRepo["owner"]["name"], url=bestRepo["owner"]["html_url"], icon_url=bestRepo["owner"]["avatar_url"])
    await interaction.response.send_message(embed=embed, ephemeral=False)
