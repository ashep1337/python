import os

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("/home/ashep/Documents/Discord_bot_creds.env")

TOKEN = os.getenv("TOKEN")
MY_USER_ID = os.getenv("MY_USER_ID")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

weather_url = os.getenv("weather_url")
api_key = os.getenv("api_key")

weather_params = {
    "lat": 42.463249,
    "lon": -92.272079,
    "appid": api_key,
    "cnt": 4,
    "units": "imperial",
}

response = requests.get(url=weather_url, params=weather_params)
data = response.json()
weather_id = []

intents = discord.Intents.default()
intents.messages = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

for n in data["list"]:
    weather_id.append(n["weather"][0]["id"])


def check_rain():
    for n in weather_id:
        if n > 700:
            return True
        else:
            return False


message = f"({data['list'][0]['dt_txt']}\n{
    data['list'][0]['weather'][0]['description']
}\nTemp: {data['list'][0]['main']['temp']} Feels like: {
    data['list'][0]['main']['feels_like']
}"


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


message = f"<@1236143565361516575>\nRain Expected\n{data['list'][0]['dt_txt']}\n{
    data['list'][0]['weather'][0]['description']
}\nTemp: {data['list'][0]['main']['temp']} Feels like: {
    data['list'][0]['main']['feels_like']
}"

if check_rain():
    bot.run(TOKEN)
else:
    print("No rain today")


# TODO: This code is written to meet the requirements for 100 DOC challenge but is slightly modified to give a weather update with the current weather conditions. I would like to make this a lot more useful and give the bot the ability to call this script when sent a message as well as add in a few more details. The initial project is to just sent an SMS text via twilio if it detects rain....

# TODO: .... in the next 12 hours, however I would like this to do a lot more and plan to build it out more in the future

# TODO: #1: Real TODO: Add function to run when user sends bot a message in discord
# TODO: #2: Add function to display an onscreen notification with notify-send
# TODO: #3 Attach to my "stats" command in order to get weather data when checking my system stats and build out stats with more useful at a glance metrics as well (like stock prices and possibly other useful tools)
