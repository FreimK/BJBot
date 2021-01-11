import discord
import os
from discord import utils
from discord.ext import commands


TOKEN = "Nzk1MzI5NDMxNDYzMjY0MjU2.X_HyQA.Kr33fAw-E5owkMjYAxYQp7Jf7eQ"


client = discord.Client()
bot = commands.Bot(command_prefix='!')

ROLES = {
    '🔨': 725762419011485766,    # R6S
    '🤡': 733335734290743438,    # Dota 2
    '🕵': 797921418201006140,    # Among Us
    '💀': 797922315416371212,    # Dead by Daylight
    '🚗': 797922938171031582,    # Rocket League
}

main_guild: int


ban = ['хуй', 'пизда', 'джигурда']  # Можешь ещё слов добавить



@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    client.main_guild = utils.get(client.guilds)
    print(client.main_guild)


@client.event
async def on_raw_reaction_add(payload):
    member = payload.member
    if payload.message_id == 795336952022958130:
        try:
            emoji = str(payload.emoji)  # эмоджик который выбрал чувак
            role = utils.get(client.main_guild.roles, id=ROLES[emoji])  # объект выбранной роли
            channel = client.get_channel(payload.channel_id)  # объект канала
            message = await channel.fetch_message(payload.message_id)  # берется объект сообщения
            if role in member.roles:  # Если у человека уже есть эта роль
                await member.remove_roles(role, reason="Bot action")  # Бот её забирает
                print(f"{member} потерял роль {role}")
            else:  # Если нет
                await member.add_roles(role, reason="Bot action")  # Человек получает роль
                print(f"{member} получил роль {role}")
            await message.remove_reaction(emoji, member)  # удаляется реакция
        except KeyError:
            print('Не найдена роль для данного эмодзи ' + emoji)
        except Exception as e:
            print(repr(e))


# Глеб, прости пж, я создал эту ф-цию просто так, в качестве обучения
@client.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        content = message.content.lower()
        for word in ban:
            if word in content:
                await message.delete()
                await message.author.send(f'{message.author.name}, лучше такое не писать...')


client.run(TOKEN)
