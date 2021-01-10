import discord
import os
from discord import utils


TOKEN = os.environ.get("TOKEN")


client = discord.Client()

ROLES = {
    '🔨': 725762419011485766,    # R6S
    '🤡': 733335734290743438,    # Dota 2
    '🕵': 797921418201006140,    # Among Us
    '💀': 797922315416371212,    # Dead by Daylight
    '🚗': 797922938171031582,    # Rocket League
}

main_guild: int

voice = 749339969516208183


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    client.main_guild = utils.get(client.guilds, id=749339969516208179)
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


client.run(TOKEN)
