from pydoc import cli
from random import choices
from typing_extensions import Required
import discord
from discord import channel
from discord.ext import commands, tasks
from discord import client
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import time
from MongoCRUD import MongoCRUD
from DiscordQuestion import DiscordQuestion
import asyncio

client = commands.Bot(command_prefix="!")
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you 👀"))
slash = SlashCommand(client, sync_commands=True)
token = ""

@slash.slash(
    name="add",
    description="Add question(s) to top of list.",
    guild_ids=[845390667273338922],
    options=[
            create_option(
            name="list_location",
            description="Add to top of questions list?",
            required=True,
            option_type=3,
            choices=[
                create_choice(
                    name="Top of List",
                    value="Top of List"
                ),
                create_choice(
                    name="Bottom of List",
                    value="Bottom of List"
                ),
            ]
        ),
        create_option(
            name="questions",
            description="\"Question One\" \"Question Two\"",
            required=True,
            option_type=3,
        )
    ]
)
async def _add(ctx:SlashContext, list_location:str,questions:str):
    message = await ctx.send("Adding questions...")
    temp = [line for line in [line.strip() for line in questions.split("\"")] if line]
    mon = MongoCRUD()
    for i in temp:
        if list_location == "Top of List":
            dq = DiscordQuestion(i, str(ctx.author), priority=1)
        else:
            dq = DiscordQuestion(i, str(ctx.author), priority=0)
        mon.addOneQuestionToDB(dq.getAsDict())
    await message.edit(content="Question(s) added, "+str(ctx.author) +" <3")


@slash.slash(
    name="channel",
    description="Specify which channel to post daily questions to.",
    guild_ids=[845390667273338922],
    options=[
        create_option(
            name="select_channel",
            description="Specify which channel(s) to post daily questions to.",
            required=True,
            option_type=7,
        )
    ]
)
async def _channel(ctx:SlashContext, select_channel):
    channel = discord.utils.get(ctx.guild.channels, name=str(select_channel))
    channel_id = channel.id
    await ctx.send(str(channel_id))
    
@tasks.loop(seconds=2)
async def my_background_task():
    """A background task that gets invoked every 10 minutes."""
    channel = client.get_channel(845390668025298956) # Get the channel, the id has to be an int
    await channel.send('TEST!')
    
@my_background_task.before_loop
async def my_background_task_before_loop():
    await client.wait_until_ready()

my_background_task.start()
client.run(token)