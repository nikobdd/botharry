import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print ( "------------ S o m b r i o S † ダーク -------------" )
    print ( "Servidores: {} Serves".format ( str ( len ( client.servers ) ) ) )
    print ( "------------ S o m b r i o S † ダーク -------------" )
    await client.change_presence (game=discord.Game ( name='S o m b r i o S † ダーク', type=1, url='https://www.twitch.tv/S o m b r i o S † ダーク' ),status='streaming' )

            
        
        
        
@client.event
async def on_message(message):      
    if message.content.startswith(',setimage'):
         set1 = message.content.strip(',setimage')
         imagem[message.author.id] = {'imagem': set1}
         embed1 = discord.Embed(color=0x070606)
         embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
         embed1.add_field(name=f"{message.author.name}", value="👷 Pronto, senhor(a) coloquei a imagem que você pediu para ser enviada no DM dos membros\n💎 Digite ,setthumbnail (link)",inline=False)
         await client.send_message(message.channel, embed=embed1)
    if message.content.startswith(',setthumbnail'):
         set1 = message.content.strip(',setthumbnail')
         thumbnail[message.author.id] = {'thumbnail': set1}
         embed1 = discord.Embed(color=0x070606)
         embed1.set_thumbnail(url="{}".format(str(thumbnail[message.author.id]['thumbnail'])))
         embed1.set_image(url="{}".format(str(imagem[message.author.id]['imagem'])))
         embed1.add_field(name=f"{message.author.name}", value="Pronto, senhor(a) 👑 coloquei a thumbnail que você pediu para ser enviada no DM dos membros\n💎 Digite ,msg)",inline=False)
         await client.send_message(message.channel, embed=embed1)
    if message.content.lower ().startswith ( ',msg' ):
        msg = message.content.strip ( ',msg' )
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
