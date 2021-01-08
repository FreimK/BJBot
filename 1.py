import discord
from discord import utils
from convars import TOKEN

ROLES = {
    '♂️': 756976295681720500,  # Instructor
    '🗑️': 773173503829868555,  # Junkyard keeper
    '⛓️': 756976920268112024  # Leatherman
}


class Main(discord.Client):

    main_guild: int

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.main_guild = utils.get(self.guilds, id=749339969516208179)
        print(self.main_guild)

    async def on_raw_reaction_add(self, payload):
        member = payload.member
        if payload.message_id == 795336952022958130:
            try:
                emoji = str(payload.emoji)  # эмоджик который выбрал чувак
                role = utils.get(self.main_guild.roles, id=ROLES[emoji])  # объект выбранной роли
                channel = self.get_channel(payload.channel_id)  # объект канала
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


client = Main()
client.run(TOKEN)
