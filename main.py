import discord, os
from discord.ext import commands


#Client
bot = commands.Bot(
    command_prefix = '$',
    help_command=None,
    self_bot=True
)

#Register Events
@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('logged in as {}'.format(bot.user))

@bot.command()
async def stream(ctx, *, message):
    stream = discord.Streaming(
        name=message,
        url="URL"
    )
    await bot.change_presence(activity=stream)
    await ctx.message.edit(content='Your streaming status: {}'.format(message))

bot.run("TOKEN", bot=False, reconnect=True)
