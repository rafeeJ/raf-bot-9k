import discord
from discord.ext import commands
import os
from random import randrange

bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def roll(ctx, dice_size):
    n = randrange(dice_size)
    await ctx.send('You rolled a {}'.format(n + 1))

bot.run(os.environ['token'])