import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("NickList")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async  def on_message(message):
    if message.content.startswith("닉리스트"):
        pic = message.content.split(" ")[0]
        await message.channel.send(file=discord.File("NickList명령어목록.jpg"))


        if message.content.startswith("닉배틀그라운드"):
            pic = message.content.split(" ")[0]
            await message.channel.send(file=discord.File("NickList닉배틀그라운드.jpg"))

    if message.content.startswith("닉로블"):
        pic = message.content.split(" ")[0]
        await message.channel.send(file=discord.File("NickList닉로블록스.jpg"))

    if message.content.startswith("닉배그"):
        pic = message.content.split(" ")[0]
        await message.channel.send(file=discord.File("NickList닉배틀그라운드.jpg"))
        





access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
