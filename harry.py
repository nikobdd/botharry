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
        msg = message.content.strip ( '+msg' )
        embed2 = discord.Embed(title='ENVIANDO MENSAGEM...',description='🚩 `MENSAGEM ESCOLHIDA:`\n' + (msg),color=0x070404)
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url )
        await client.send_message(message.channel, embed=embed2)
        x = list ( message.server.members)
        s = 0
        for member in x:
            embed1 = discord.Embed ( title="Hogwarts", url="", color=0x070404,description=' <@{}> {}'.format ( member.id, msg ) )
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
        embed2 = discord.Embed ( title='MENSAGEM ENVIADA:',description="📥 `SUCESSO:` \nMensagem enviada com sucesso para todos membros do servidor",color=0x070404)
        embed2.set_footer ( text=client.user.name, icon_url=client.user.avatar_url )
        await client.send_message ( message.channel, embed=embed2 )
        
        
        
@client.event
async def on_member_join(member):
    role1 = "Trouxas"
    role = discord.utils.find ( lambda r: r.name == "{}".format ( role1 ), member.server.roles )
    await client.add_roles ( member, role )
    embedvindo = discord.Embed ( color=0x070404, title='Seja Bem Vindo (a)',description='🔮' + member.mention + '***ao Hogwarts Leia as #regras, Matricule-se aqui -> #:steam_locomotive:plataforma-9-34:steam_locomotive: ou #🤱chat-dos-trouxas🧙♂ Divirta-se futuro Bruxo(a)⚡***' )
    embedvindo.set_thumbnail ( url=member.avatar_url )
    embedvindo.set_author ( name=member.name, icon_url=member.avatar_url )
    mensagemvindo2 = "salão-principal"
    bemvindo = discord.utils.find ( lambda c: c.name == "{}".format ( mensagemvindo2 ), member.server.channels )
    await client.send_message ( bemvindo, embed=embedvindo )

        
        

client.run(str(os.environ.get('TOKEN')))
