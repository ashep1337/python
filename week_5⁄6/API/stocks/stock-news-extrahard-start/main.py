import json
import os
from datetime import datetime, timedelta

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("/home/ashep/Documents/Discord_bot_creds.env")

ALPHA_API = os.getenv("ALPHA_ADVANTAGE_API")
NEWSAPI = os.getenv("NEWSAPI")
TOKEN = os.getenv("TOKEN")
MY_USER_ID = os.getenv("MY_USER_ID")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": ALPHA_API,
}
alpha_url = "https://www.alphavantage.co/query"

news_params = {
    "apiKey": NEWSAPI,
    "q": "Tesla",
}

news_url = "https://newsapi.org/v2/everything"


response = requests.get(url=news_url, params=news_params)
data = response.json()

article_list = []
message = ""
for n in range(0, 3):
    article_list.append(data["articles"][n])
    message += f"Headline: {article_list[n]['title']}\n"
    message += f"Brief: {article_list[n]['description']}\n\n"

with open("stock_daily.json", "r") as data_file:
    data = json.load(data_file)

yesterday_date = datetime.now() - timedelta(days=1)
day_before_date = datetime.now() - timedelta(days=2)

yesterday_close = data["Time Series (Daily)"][str(yesterday_date.date())]["4. close"]
day_before_close = data["Time Series (Daily)"][str(day_before_date.date())]["4. close"]
percent_change = round(
    ((float(yesterday_close) - float(day_before_close)) / float(yesterday_close) * 100),
    2,
)

if 5 < percent_change or -5 > percent_change:
    intents = discord.Intents.default()
    intents.messages = True
    intents.dm_messages = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"Bot is online as {bot.user}")
        try:
            channel = bot.get_channel(CHANNEL_ID)
            if channel is None:
                print("Channel not found!")
                await bot.close()
                return
            await channel.send(message)
            print("Message sent to channel!")
        except Exception as e:
            print(f"Failed to send message: {e}")
        await bot.close()

    if 1 < percent_change or -1 > percent_change:
        print("Get News")

    bot.run(TOKEN)


# TODO: I would like to make this follow my personal stocks and give more than just news. I'm not sure how I will improve this but I think I would like to add inputs to query the exact data for news and stocks I would like to get. Maybe be able to ask for news on a certain stock or find all breaking news. Maybe query price changes for stocks based on user input
