import discord
from discord.ext import commands

import os
import re
from random import randrange

bot = commands.Bot(command_prefix='$')

@bot.command()
async def roll(ctx, dice_size):
    result = re.match('d(\d{1,8})', dice_size, flags=re.IGNORECASE)
    if result:
        dice_to_roll = int(result.group(1))
        if dice_to_roll == 0:
            await ctx.send('Stop trying to roll a 0', delete_after=5)
            return False
        rolled_number = randrange(dice_to_roll) + 1
        if rolled_number == dice_to_roll and dice_to_roll != 1:
            await ctx.send('Oh baby, a natural {}!'.format(rolled_number), file=discord.File('imgs/nat.gif'))
        elif rolled_number == 1 and dice_to_roll != 1:
            await ctx.send('Hhahaha natural {} hahahah'.format(rolled_number), file=discord.File('imgs/fail.gif'))
        else:
            await ctx.send('You rolled a {}'.format(rolled_number))
    else:
        await ctx.send('Syntax is: $roll d<number>', delete_after=5)

bot.run(os.environ['token'])