import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '/give_role':
        member = message.author
        role = member.guild.get_role(ID_ROLE_MEMBER)
        await member.add_roles(role)
        await message.delete()
    if message.content == '/clean':
        Ch = message.channel.id
        if Ch == 796382696330756126 or Ch == 796383874069430282:
            await message.channel.purge(limit=None)

@client.event
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
