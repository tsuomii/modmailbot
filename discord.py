import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix='.', intents=intents)

OWNER_ID = 687445638950027269  # <-- Replace with your user ID (as an integer)

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.command()
async def help(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        await ctx.send(
            "_ _ 𓎢𓎡 ㅤ<:003_blackbow:1353004138782527570>  ㅤ⊹ㅤ**support/help form**  **!** *!*\n"
            "-# ㅤㅤㅤㅤㅤplease tell us how we can assist you\n\n"
            "- type of help/support needed:\n"
            "- explain the issue:\n"
            "- additional details (if any):\n\n"
            "Please respond in this format separated by `|`:\n"
            "`type of help | explanation | additional details`"
        )

        def check(m):
            return m.author == ctx.author and isinstance(m.channel, discord.DMChannel)

        try:
            msg = await bot.wait_for("message", check=check, timeout=300)
            parts = msg.content.split("|")

            if len(parts) < 2:
                await ctx.send("⚠️ Format error. Use `|` to separate each part.")
                return

            type_help = parts[0].strip()
            explanation = parts[1].strip()
            additional = parts[2].strip() if len(parts) > 2 else "None"

            owner = await bot.fetch_user(OWNER_ID)
            await owner.send(
                f"📩 **New Support Request from {ctx.author}**\n\n"
                f"**Type of Help:** {type_help}\n"
                f"**Explanation:** {explanation}\n"
                f"**Additional Details:** {additional}"
            )

            await ctx.send("✅ Thank you! Your request has been sent.")

        except Exception as e:
            await ctx.send("⏳ You took too long to respond or something went wrong.")
            print(f"Error: {e}")

@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel) and message.content.lower().startswith('.help'):
        ctx = await bot.get_context(message)
        await bot.invoke(ctx)
    else:
        await bot.process_commands(message)

bot.run("MTM5MzI5OTM2MTU1MDgyNzU2MQ.GW6gHu.unimxmZaETxFukNj2WViC1liyK6oFzzLTA6ZhM")  
