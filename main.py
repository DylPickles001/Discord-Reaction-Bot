import discord
import os
from keep_alive import keep_alive

intent = discord.Intents.all()
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#action by bot
@client.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if message_id == 790494357705981952:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

    if payload.emoji.name == 'ultimate':
      role = discord.utils.get(guild.roles, name='ultimate')
    elif payload.emoji.name == 'melee':
      role = discord.utils.get(guild.roles, name='melee')
    else:
      role = discord.utils.get(guild.roles, name= payload.emoji.name)  

    if role is not None:
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
      if member is not None:
        await member.add_roles(role)
        print('done')
      else:
        print('Member not found')
    else: 
      print('Role not found')

@client.event
async def on_raw_reaction_remove(payload):
  pass

#runs bot
keep_alive()
client.run(os.getenv('TOKEN'))