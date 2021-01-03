import os
import discord
from discord import utils

token = ''

id = 795336952022958130

roli = {
    '♂️': 756976295681720500, #Instructor
    '🗑️': 773173503829868555, #Junkyard keeper
    '⛓️': 756976920268112024 #Leatherman
}
count = ()


class Main(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == id:
            channel = self.get_channel(payload.channel_id) # получаем объект канала
            message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
            member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию


    async def giving(self, member):
            try:
                emoji = str(payload.emoji) # эмоджик который выбрал чувак
                role = utils.get(message.guild.roles, id=roli[emoji]) # объект выбранной роли
                await member.add_roles(role) # человек получает роль
                print('{0.display_name} была выдана роль {1.name} в нашем gym'.format(member, role))

            except KeyError as e:
                print('Не найдена роль для данного эмодзи'+ emoji)
            except Exception as e:
                print(repr(e))


    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id) # получаем объект канала
        message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
        member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию

    async def removing(self, member):
        try:
            emoji = str(payload.emoji) # эмоджик который выбрал чувак
            role = utils.get(message.guild.roles, id=roli[emoji]) # объект выбранной роли

            await member.remove_roles(role)
            print('Billy забрал у {0.display_name} роль {1.name}'.format(member, role))

        except KeyError as e:
            print('Не найдена роль для данного эмодзи' + emoji)
        except Exception as e:
            print(repr(e))


client = Main()
client.run(token)
