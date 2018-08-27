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
    print ( "------------ S o m b r i o S † ダーク -------------" )
    print ( "Servidores: {} Serves".format ( str ( len ( client.servers ) ) ) )
    print ( "------------ S o m b r i o S † ダーク -------------" )
    await client.change_presence (game=discord.Game ( name='S o m b r i o S † ダーク', type=1, url='https://www.twitch.tv/S o m b r i o S † ダーク' ),status='streaming' )

            
        
        
        
@client.event
async def on_message(message):      
    if message.content.startswith('s,setimage'):
         set1 = message.content.strip('s,setimage')
         imagem[message.author.id] = {'imagem': set1}
         embed1 = discord.Embed(color=0x070606)
         embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
         embed1.add_field(name=f"{message.author.name}", value="👷 Pronto, senhor(a) coloquei a imagem que você pediu para ser enviada no DM dos membros\n💎 Digite s,setthumbnail (link)",inline=False)
         await client.send_message(message.channel, embed=embed1)
    if message.content.startswith('s,setthumbnail'):
         set1 = message.content.strip('s,setthumbnail')
         thumbnail[message.author.id] = {'thumbnail': set1}
         embed1 = discord.Embed(color=0x070606)
         embed1.set_thumbnail(url="{}".format(str(thumbnail[message.author.id]['thumbnail'])))
         embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
         embed1.add_field(name=f"{message.author.name}", value="Pronto, senhor(a) 👑 coloquei a thumbnail que você pediu para ser enviada no DM dos membros\n💎 Digite s,msg)",inline=False)
         await client.send_message(message.channel, embed=embed1)
    if message.content.lower ().startswith ( 's,msg' ):
        msg = message.content.strip ( 's,msg' )
        embed2 = discord.Embed(title='ENVIANDO MENSAGEM...',description='🚩 `MENSAGEM ESCOLHIDA:`\n' + (msg),color=0x070606)
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url )
        await client.send_message(message.channel, embed=embed2)
        x = list ( message.server.members)
        s = 0
        for member in x:
            embed1 = discord.Embed ( title="S o m b r i o S † ダーク", url="", color=0x070606,description=' <@{}> {}'.format ( member.id, msg ) )
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
        embed2 = discord.Embed ( title='MENSAGEM ENVIADA:',description="📥 `SUCESSO:` \nMensagem enviada com sucesso para todos membros do servidor",color=0x070606)
        embed2.set_footer ( text=client.user.name, icon_url=client.user.avatar_url )
        await client.send_message ( message.channel, embed=embed2 )

client.run(str(os.environ.get('TOKEN')))
