import discord
from discord.ext import commands
from TourParticipant import TourParticipant
from TFTTour import TFTTour

bot = commands.Bot(command_prefix="!")
active_tours = []


@bot.command()
async def init_tour(ctx, name):
    """Initiates a TFTTour."""
    role = await ctx.guild.create_role(name=f"{name} participant")

    overwrites_chat = {ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                       role: discord.PermissionOverwrite(read_messages=True)}
    overwrites_general = {ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                          role: discord.PermissionOverwrite(read_messages=True)}
    overwrites_commands = {ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False)}
    cat = await ctx.guild.create_category_channel(name)
    com = await ctx.guild.create_text_channel(f"{name}_commands", category=cat, overwrites=overwrites_commands)
    log = await ctx.guild.create_text_channel(f"{name}_log", category=cat, overwrites=overwrites_general)
    res = await ctx.guild.create_text_channel(f"{name}_results", category=cat, overwrites=overwrites_general)
    scor = await ctx.guild.create_text_channel(f"{name}_scoring", category=cat, overwrites=overwrites_general)
    chat = await ctx.guild.create_text_channel(f"{name}_chat", category=cat, overwrites=overwrites_chat)
    active_tours.append(TFTTour(name, [com.id, log.id, res.id, scor.id, chat.id], role.id))


@bot.command()
async def end_tour(ctx):
    """Ends a TFTTour. Will be made accessible only after tour completion after project completion."""
    c_id = ctx.channel.id
    for t in active_tours:
        if t.get_command_channel() == c_id:
            tour = t
            break
    else:
        return await ctx.send("This is not the commands channel of an active tour!")
    await bot.get_channel(ctx.channel.category_id).delete()
    await bot.get_channel(tour.get_command_channel()).delete()
    await bot.get_channel(tour.get_log_channel()).delete()
    await bot.get_channel(tour.get_results_channel()).delete()
    await bot.get_channel(tour.get_scoring_channel()).delete()
    await bot.get_channel(tour.get_chat_channel()).delete()
    active_tours.remove(tour)

with open('files/key.txt') as key_file:
    bot_key = key_file.readline()
    key_file.close()
bot.run(bot_key)
