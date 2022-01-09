from random import choices
from typing_extensions import Required
import discord
from discord.ext import commands
from discord import client
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)
token = "OTI3OTcyNjA5MDEyOTI4NTEy.YdR_1g.6zMkvZ7wdaOs22F01LXg2jQGdIs"

@slash.slash(
    name="add",
    description="Add question(s) to top of list.\"Question One\" \"Question Two\"",
    guild_ids=[845390667273338922],
    options=[
        create_option(
            name="option",
            description="Add to top of questions list?",
            required=True,
            option_type=3,
        )
    ]
)
async def _add(ctx:SlashContext, option:str):
    await ctx.send(option)

# @slash.slash(
#     name="add",
#     description="Add question(s) to top of list.\"Question One?\" \"Question Two?\"",
#     guild_ids=[845390667273338922],
#     options=[
#         create_option(
#             name="option",
#             description="Add to top of questions list?",
#             required=True,
#             option_type=3,
#             choices=[
#                 create_choice(
#                     name="True",
#                     value="True"
#                 ),
#                 create_choice(
#                     name="False",
#                     value="False"
#                 ),
#             ]
#         )
#     ]
# )
# async def _add(ctx:SlashContext, option:str):
#     await ctx.send(option)

client.run(token)