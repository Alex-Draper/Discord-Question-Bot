import discord
from discord.ext import commands
import random

from discord.ext.commands.core import bot_has_any_role

description = """An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here."""

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="/", description=description, intents=intents)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


@bot.command()
async def addQuestion(ctx, *questions: str):
    count = 0
    new_questions = []
    for i in questions:
        new_questions[count] = i
        count += 1
    # Add questions to database, right after all the previously asked questions so that the newly added one is picked next


# @bot.command()
# async def add(ctx, left: int, right: int):
#     """Adds two numbers together."""
#     await ctx.send(left + right)


# @bot.command()
# async def roll(ctx, dice: str):
#     """Rolls a dice in NdN format."""
#     try:
#         rolls, limit = map(int, dice.split("d"))
#     except Exception:
#         await ctx.send("Format has to be in NdN!")
#         return

#     result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
#     await ctx.send(result)


# @bot.command(description="For when you wanna settle the score some other way")
# async def choose(ctx, *choices: str):
#     """Chooses between multiple choices."""
#     await ctx.send(random.choice(choices))


# @bot.command()
# async def repeat(ctx, times: int, content="repeating..."):
#     """Repeats a message multiple times."""
#     for i in range(times):
#         await ctx.send(content)


# @bot.command()
# async def joined(ctx, member: discord.Member):
#     """Says when a member joined."""
#     await ctx.send("{0.name} joined in {0.joined_at}".format(member))


# @bot.group()
# async def cool(ctx):
#     """Says if a user is cool.
#     In reality this just checks if a subcommand is being invoked.
#     """
#     if ctx.invoked_subcommand is None:
#         await ctx.send("No, {0.subcommand_passed} is not cool".format(ctx))


# @cool.command(name="bot")
# async def _bot(ctx):
#     """Is the bot cool?"""
#     await ctx.send("Yes, the bot is cool.")


bot.run("OTI3OTcyNjA5MDEyOTI4NTEy.YdR_1g.6zMkvZ7wdaOs22F01LXg2jQGdIs")