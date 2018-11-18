from discord.ext import commands
import discord
import os
import random
import Music

#############################################
#~~~~~~~~~~~~~~~~~~~SETUP~~~~~~~~~~~~~~~~~~~#
#############################################
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), description='A playlist example for discord.py')
bot.add_cog(Music.Music(bot))

#############################################
#~~~~~~~~~~~~~~~~~~~EVENT~~~~~~~~~~~~~~~~~~~#
#############################################
@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    if (left, right) in [(9, 10), (10, 9)]:
        await bot.say(21)
    else:
        await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for _ in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))
    
@bot.command(pass_context = True)
async def roulette(ctx):
    loser = random.choice([i for i in ctx.message.server.members])
    em = discord.Embed(color = 0x7fffd4).set_image(url=loser.avatar_url)
    em.add_field(name='Loser', value=str(loser))
    await bot.say(embed = em)

@bot.command(pass_context = True)
async def test(ctx):
    await bot.say('Nothing to look at over here, mind your buisness')
#############################################
#~~~~~~~~~~~~~~~~~ON READY~~~~~~~~~~~~~~~~~~#
#############################################
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(os.environ["BOT_TOKEN"])
