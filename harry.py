import random
import discord
import asyncio
import json
import time
import datetime
import safygiphy
import io
import os

client = discord.Client()
g = safygiphy.Giphy ()
COR = 0x00f80c


imagem = {'000000000000000000': {'imagem': 0}}
thumbnail = {'000000000000000000': {'thumbnail': 0}}

@client.event
async def on_ready():
    print ( "------------Hogwarts-------------" )
    print ( "Servidores: {} Serves".format ( str ( len ( client.servers ) ) ) )
    print ( "------------ Hogwarts -------------" )
    await client.change_presence(game=discord.Game(name=" {} 🔮Alunos🔮 ".format(str(len(set(client.get_all_members())))), type=1, url='https://www.twitch.tv/shiro'),status='streaming')
            
        
        
        
@client.event
async def on_message(message):      
    if message.content.startswith('+setimage'):
         set1 = message.content.strip('+setimage')
         imagem[message.author.id] = {'imagem': set1}
         embed1 = discord.Embed(color=0x070404)
         embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
         embed1.add_field(name=f"{message.author.name}", value="👷 Pronto, senhor(a) coloquei a imagem que você pediu para ser enviada no DM dos membros\n💎 Digite +setthumbnail (link)",inline=False)
         await client.send_message(message.channel, embed=embed1)
    if message.content.startswith('+setthumbnail'):
         set1 = message.content.strip('+setthumbnail')
         thumbnail[message.author.id] = {'thumbnail': set1}
         embed1 = discord.Embed(color=0x070404)
         embed1.set_thumbnail(url="{}".format(str(thumbnail[message.author.id]['thumbnail'])))
         embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
         embed1.add_field(name=f"{message.author.name}", value="Pronto, senhor(a) 👑 coloquei a thumbnail que você pediu para ser enviada no DM dos membros\n💎 Digite +msg)",inline=False)
         await client.send_message(message.channel, embed=embed1)
    if message.content.lower ().startswith ( '+msg' ):
        role = discord.utils.get(message.server.roles, name='Argo Filch')
        if not role in message.author.roles:
         embed1 = discord.Embed(title="SEM PERMISSÃO", description="Você precisa do cargo ADM",color=0x070404)
         return await client.send_message(message.channel, embed=embed1)
        msg = message.content.strip ( '+msg')
        embed2 = discord.Embed(title='ENVIANDO MENSAGEM...',description='🚩 `MENSAGEM ESCOLHIDA:`\n' + (msg),color=0x070404)
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url )
        await client.send_message(message.channel, embed=embed2)
        x = list ( message.server.members)
        s = 0
        for member in x:
            embed1 = discord.Embed ( title="Hogwarts", url="", color=0x070404,description=' <@{}> {}'.format(member.id, msg))
            embed1.set_thumbnail(url="{}".format(str(thumbnail[message.author.id]['thumbnail'])))
            embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
            embed1.set_footer ( text=client.user.name, icon_url=client.user.avatar_url )
            try:
                await client.send_message ( member, embed=embed1 )
                print ( member.name )
                s += 1
            except:
                pass
        print ( '\nAviso enviado para {} membros de {}'.format ( s, len ( x ) ) )
        embed2 = discord.Embed ( title='MENSAGEM ENVIADA:',description="📥 `SUCESSO:` \nMensagem enviada com sucesso para todos membros do servidor",color=0x9e00f3)
        embed2.set_footer ( text=client.user.name, icon_url=client.user.avatar_url )
        await client.send_message ( message.channel, embed=embed2 )
        


        
@client.event
async def on_member_join(member):
  embed1 = discord.Embed(color=0x070404, description='***Hogwarst***')
  embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
  embed1 = discord.Embed ( title="\n<:hogwarts2:482966802020696065> Escola de Magia e Bruxaria De Hogwarts <:hogwarts2:482966802020696065>\n", url="", color=0x474545,description='***\nDiretor: Albus Dumbledore\n Coordenadores das casas Grifinória, Sonserina, Lufa lufa, Corvinal\n\n\n*** Prezado(a) {}'.format(member.mention))
  embed1.add_field(name="***\nTemos o prazer de informar que você foi aceito na escola de Magia e Bruxaria de Hogwarts.***",value="*** Estamos anexando uma lista dos livros e equipamentos necessários.Para se matricular, vá nos canais de voz (Expresso) e entre em contato com algum Chapéu Seletor ou Elfo Doméstico , caso queria realizar sua matrícula por voz, basta responder as perguntas da <#482966802020696065> , em seguida compre seu material nas <#482966802020696065> Torne-se o bruxo(a) mais poderoso da história!\n\n\n Atenciosamente;\n\n\n DIRETORIA DE HOGWARST***",inline=False)
  embed1.set_image(url="https://cdn.discordapp.com/attachments/479093968139976706/484127778107686924/logo22.png")
  await client.send_message(member,embed=embed1)



client.run(str(os.environ.get('TOKEN')))
