import discord
from discord.ext import commands

bot = commands("!")


@bot.event
async def on_ready():
      print(f"MIMDE PAPAI {bot.user}")
@bot.event
async def on_message(message):
        if message.author == bot.user:
            return
        if "não" in message.content:
            await message.channel.send(f"MIM DE FARINHA,{message.author.name}, OU VOU TE PEGAR HOJE DE NOITE")

            await bot.process_command(message)





@bot.command(name ="oi")
async def pedir_farinha(ctx):
  name = ctx.author.name
  reposta = "Me dê!" + name
  await ctx.send(reposta)

bot.run("")
