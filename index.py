# import interactions
# import discord
# from discord.ext.commands import Bot

# bot = interactions.Client(token="OTI3OTcyNjA5MDEyOTI4NTEy.YdR_1g.6zMkvZ7wdaOs22F01LXg2jQGdIs")


# @bot.command(
#     name="test",
#     description="this is just a test command.",
#     scope=845390667273338922
# )
# async def test(ctx):
#     await ctx.send("Hello world!")

# @bot.command(
#     name="test2",
#     description="this is just a test command.",
#     scope=845390667273338922
# )
# async def test(ctx):
#     await ctx.send("Hello world!")



# bot.start()

import disnake

client = disnake.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTI3OTcyNjA5MDEyOTI4NTEy.YdR_1g.6zMkvZ7wdaOs22F01LXg2jQGdIs')