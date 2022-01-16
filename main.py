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
slash = SlashCommand(client, sync_commands=True)
token = "OTI3OTcyNjA5MDEyOTI4NTEy.YdR_1g.6zMkvZ7wdaOs22F01LXg2jQGdIs"

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
    # await ctx.message.add_reaction(":thumbsup")
    await ctx.send("Adding questions...")
    # await ctx.deferred
    # await ctx.defer
    temp = [line for line in [line.strip() for line in questions.split("\"")] if line]
    mon = MongoCRUD()
    for i in temp:
        if list_location == "Top of List":
            dq = DiscordQuestion(i, str(ctx.author), priority=1)
        else:
            dq = DiscordQuestion(i, str(ctx.author), priority=0)
        mon.addOneQuestionToDB(dq.getAsDict())
    # await ctx.message.edit("Questions added, "+str(ctx.author) +" <3")
    await ctx.send("Questions added, "+str(ctx.author) +" <3")
    
client.run(token)