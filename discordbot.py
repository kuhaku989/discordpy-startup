from discord.ext import commands
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='/')

@bot.event
async def on_message(message):
    try:
        if message..author.bot:
            return
        await bot.process_commands(message)
    except Exception:
        await meesage.channel.send(f'```\n{traceback.format_exc()}\n```')
    
@bot.commands
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
