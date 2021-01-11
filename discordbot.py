import discord
from discord.ext import commands
import random
import sys
import asyncio
import re
import os

token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='/')
ID_ROLE_MEMBER = 796380696812716102 # 付けたい役職のID(int)

@bot.command()
async def give_role(ctx):
    member = message.author
    role = member.guild.get_role(ID_ROLE_MEMBER)
    await member.add_roles(role)
    await message.delete()

@bot.command()
async def clean(ctx):
    Ch = message.channel.id
    if Ch == 796382696330756126 or Ch == 796383874069430282:
        await message.channel.purge(limit=None)

@bot.command()
async def on_voice_state_update(member, before, after):
     if not before.channel and after.channel:
        set_mention_name = after.channel.name
        role1 = discord.utils.get(member.guild.roles, name=set_mention_name)
        await member.add_roles(role1)
     elif before.channel and not after.channel:
        remove_mention_name = before.channel.name
        role1 = discord.utils.get(member.guild.roles, name=remove_mention_name)
        await member.remove_roles(role1)
 
bot.run(token)
