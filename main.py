import discord
from os import listdir
from discord.ui import Button, View
from discord import Embed, file
from discord.ext import commands

token="" #Put your discord token there

client = commands.Bot(command_prefix ="$") #you can change prefix to whatever you want 
client.remove_command('help')

@client.command()
async def search(ctx, arg1):
    await ctx.message.delete()
    embed=discord.Embed(color=0x39fd3f)
    embed.set_author(name="Olympus Coding Service", url="https://cracked.to/Wntd")
    embed.set_thumbnail(url="https://i.pinimg.com/originals/40/55/da/4055da716e80ffef4742b05d40dce139.png")
    embed.add_field(name="Searching File now", value="Results for **"+arg1+"**...", inline=False)
    await ctx.send(embed=embed)
    search = open("C:/Users/Range/Desktop/test/dumps.txt") #Your path to the file you want the bot to search for
    for line in search:
        if arg1 in line:
            embed=discord.Embed(color=0x39fd3f)
            embed.add_field(name="Data Search", value=line, inline=False)
            await ctx.send(embed=embed)
client.run(token)
