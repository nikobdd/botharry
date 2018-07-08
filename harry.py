import random
import discord
import asyncio
from discord.utils import get
import requests
import json
from random import randint

client = discord.Client()
@client.event
async def on_ready():
    print("------------?  S P E C T R U M  ?-------------")
    print("Servidores: {} Serves".format(str(len(client.servers))))
    print("------------?  S P E C T R U M  ?-------------")
    await client.change_presence(game=discord.Game(name=',ajuda', type=1, url='https://www.twitch.tv/eabot'),status='streaming')

@client.event
async def on_message(message):
    if message.content.lower().startswith("harry,ban"):
        try:

            if not message.author.server_permissions.administrator:
                return await client.send_message(message.channel, ' <:tane:457629062064635905>?Permissão Insuficiente')
            author = message.author.mention
            user = message.mentions[0]
            embed1 = discord.Embed(color=0xff0101)
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            embed1.set_image(url="https://d2118lkw40i39g.cloudfront.net/wp-content/uploads/2016/09/harry-potter-dementor-giphy.gif")
            await client.ban(user)
            embed1.add_field(name="<:boxing_glove:457628939641421824> **??? ?s?l?**",value='{}***Foi Banido Com Sucesso Senhor***: **{}**'.format(user.mention, author))
            embed1.set_image(url="https://d2118lkw40i39g.cloudfront.net/wp-content/uploads/2016/09/harry-potter-dementor-giphy.gif")
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=embed1)
        except discord.errors.Forbidden:
            return await client.send_message(message.channel,'<:crossed_swords:457638598607503360> **|** ***Infelizmente o cargo do usuario mencionado e maior que o meu , ou ele é um administrador***.')




    if message.content.startswith(',setar'):
        set1 = message.content.strip(',setar')
        global setar
        setar = set1

    if message.content.lower().startswith(',msg'):
        role = discord.utils.get(message.server.roles, name='BotHarry')
        if not role in message.author.roles:
            embed1 = discord.Embed(title='OCORREU UM ERRO:', description="<:no:440061539026731008> `SEM PERMISSÃO:` Você precisa do cargo `Harry`",color=0xff0101)
            embed1.set_footer(text="?  S P E C T R U M  ?", icon_url="https://i.imgur.com/320SovU.png")
            return await client.send_message(message.channel, embed=embed1)
        msg = message.content.strip(',msg')
        embed2 = discord.Embed(title='ENVIANDO MENSAGEM...',description='<:conometro:449635557753094164> `MENSAGEM ESCOLHIDA:`\n' + (msg),color=0xff0101)
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)
        x = list(message.server.members)
        s = 0
        for member in x:
            embed1 = discord.Embed(title="Aviso Do Servidor: ?  S P E C T R U M  ?", url="", color=0xff0101,description=' <@{}> {}'.format(member.id, msg))
            embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/434485929735094274/456220288510722070/320SovU.png")
            embed1.set_image(url="")
            embed1.set_image(url=setar)
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            try:
                await client.send_message(member, embed=embed1)
                print(member.name)
                s += 1
            except:
                pass
        print('\nAviso enviado para {} membros de {}'.format(s, len(x)))
        embed2 = discord.Embed(title='MENSAGEM ENVIADA:',description="<:ok:440061516365037569> `SUCESSO:` \nMensagem enviada com sucesso para todos membros do servidor",color=0xff0101)
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)
        
        
client.run(str(os.environ.get('TOKEN')))
