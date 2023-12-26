token = "YOUR_TOKEN_HERE"
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.author != self.user:
            await message.channel.send("Thanks for your message!")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)