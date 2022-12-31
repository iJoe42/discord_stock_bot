import interactions
import os
from dotenv import load_dotenv
import ReqSettrade

def main():

    load_dotenv("DISCORD_TOKEN.env")
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    bot = interactions.Client(token=DISCORD_TOKEN)

    @bot.event
    async def on_ready():
        print("Success: Bot is connected to Discord")

    """
    @bot.command(
        name="alert",
        description="Stock Alert"
    )
    async def alert(ctx: interactions.CommandContext):
        embed_msg = "put embed message here" #call function here
        await ctx.channel.send(embeds=embed_msg)
    """

    @bot.command(
        name="top_gainer",
        description="Current Top Gainer",
        options=[interactions.Option(
            name="number",
            description="Number of top gainer stocks",
            type=interactions.OptionType.INTEGER,
            required=True,
        )],
    )
    async def top_gainer(ctx: interactions.CommandContext, number: int):
        embed_msg = ReqSettrade.fetch_top_gainer(number)
        await ctx.channel.send(embeds=embed_msg)

    @bot.command(
        name="top_loser",
        description="Current Top Loser",
        options=[interactions.Option(
            name="number",
            description="Number of top loser stocks",
            type=interactions.OptionType.INTEGER,
            required=True,
        )],
    )
    async def top_loser(ctx: interactions.CommandContext, number: int):
        embed_msg = ReqSettrade.fetch_top_loser(number)
        await ctx.channel.send(embeds=embed_msg)

    bot.start()

if __name__ == "__main__":
    main()