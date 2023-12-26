import discord
import requests
from bs4 import BeautifulSoup
import asyncio
import tokens

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

async def check_news():
    await client.wait_until_ready()
    channel = client.get_channel(tokens.CHANNEL_ID)
    while not client.is_closed():
        try:
            page = requests.get("https://ridmik.news/latest")
            soup = BeautifulSoup(page.content, "html.parser")
            news_container = soup.find(id="__next")
            latest_news_elements = news_container.find_all("div", class_="title")

            for title_element in latest_news_elements:
                title_text = title_element.find("a").get_text(strip=True)
                summary_element = title_element.find_next_sibling("div", class_="summary")
                summary_text = summary_element.get_text(strip=True) if summary_element else 'No summary available'
                
                # Send the news to the Discord channel
                await channel.send(f"**{title_text}**\n{summary_text}\n")
            
            # Wait for 5 minutes before checking again
            await asyncio.sleep(300)
        except Exception as e:
            print(f"An error occurred: {e}")
            await asyncio.sleep(300)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    client.loop.create_task(check_news())

client.run(tokens.TOKEN)