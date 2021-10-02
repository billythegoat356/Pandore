from discord.ext import commands




token = "your bots token"
gitbot = commands.Bot(command_prefix='>')



@gitbot.command()
async def ping(ctx):
    return await ctx.channel.send(content="pong!")



gitbot.run(token)
