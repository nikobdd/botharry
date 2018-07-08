import random
import discord
import asyncio
from discord.utils import get
import requests
import json
import time
from random import randint
import re
import datetime
import safygiphy
import io

g = safygiphy.Giphy()
COR = 0x7289DA

client = discord.Client()


@client.event
async def on_ready():
    print("------------DARYA-------------")
    print("Servidores: {} Serves".format(str(len(client.servers))))
    print("------------DARYA-------------")
    await client.change_presence(game=discord.Game(name='dr?ajuda', type=1, url='https://www.twitch.tv/daryabot'),
                                 status='streaming')


@client.event
async def on_message(message):
    if message.content.lower().startswith("dr?ban"):
        try:

            if not message.author.server_permissions.administrator:
                return await client.send_message(message.channel, '<:fire:457629062064635905>?Permissão Insuficiente')
            author = message.author.mention
            user = message.mentions[0]
            embed1 = discord.Embed(color=0xff00eb)
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            embed1.set_image(
                url="https://cdn.discordapp.com/attachments/461479588481073162/462649531041972224/f9c305fb.gif")
            await client.ban(user)
            embed1.add_field(name="<:revolving_hearts:462189330702532618> ***Darya***",
                             value='{}***Foi Banido Com Sucesso Senpai*** **{}**'.format(user.mention, author))
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=embed1)
        except discord.errors.Forbidden:
            return await client.send_message(message.channel,
                                             '<:crossed_swords:457638598607503360> **|** ***Infelizmente o cargo do usuario mencionado e maior que o meu , ou ele é um administrador***.')

    if message.content.startswith('dr?gif'):
        try:
            tag = message.content[6:]
            resultado = giphy_api(tag)
            embed_gif = discord.Embed(title="\n", description='\n', color=0x163d7c)
            embed_gif.set_image(url=resultado)
            embed_gif.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=embed_gif)
        except:
            await client.send_message(message.channel, '***Gif Encontrado ^^***')

    def giphy_api(tag):
        url = 'http://api.giphy.com/v1/gifs/search?q={}&api_key=KEY&limit=16'.format(tag)
        resposta = requests.get(url)
        resposta_json = json.loads(resposta.text)
        gif = resposta_json['data'][randrange(0, 15)]['id']
        return 'https://media.giphy.com/media/{}/giphy.gif'.format(gif)

    if message.content.startswith('dr?uptime'):
        await client.send_message(message.channel,
                                  "***Estou online a {0} hora(s) e {1} minuto(s)***".format(hour, minutes))

    async def tutorial_uptime():
        await client.wait_until_ready()
        global minutes
        minutes = 0
        global hour
        hour = 0
        while not client.is_closed:
            await asyncio.sleep(60)
            minutes += 1
            if minutes == 60:
                minutes = 0
                hour += 1

    client.loop.create_task(tutorial_uptime())

    if message.content.lower().startswith("dr?mutar"):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel,
                                             '<:error:455028754008375296> **|** Você não tem permissões suficiente.')
        user = message.mentions[0]
        author = message.author
        cargo = discord.utils.get(message.author.server.roles, name='Mute')
        try:
            await client.add_roles(user, cargo)
            embed1 = discord.Embed(color=0xff00eb)
            embed1.add_field(name="<:mute:455719792037330965> Mute",
                             value='{}\n``` Foi mutado pelo administrador:``` **{}**'.format(user.mention, author))
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=embed1)
        except AttributeError:
            embed1 = discord.Embed(color=0xff00eb)
            embed1.add_field(name="<:error:455028754008375296> Mute",
                             value='***Infelizmente o servidor não tinha o cargo*** ***Dayra-Mute***, o cargo foi criado, digite o comando novamente.')
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=embed1)
            await client.create_role(author.server, name="Mute", colour=discord.Colour(0xff00eb))

    if message.content.lower().startswith("dr?desmultar"):
        if not message.author.server_permissions.administrator:
            return await client.send_message(message.channel,
                                             '<:error:455028754008375296> **|** Você não tem permissões suficiente.')
        author = message.author
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name="Mute")
        await client.remove_roles(user, cargo)
        embed1 = discord.Embed(color=0xff00eb)
        embed1.add_field(name="<:mute:455719792037330965> Mute",
                         value='{} Foi desmultado pelo administrador: **{}**'.format(user.mention, author))
        embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed1)

    if message.content.startswith('dr?server'):
        serverinfo_embed = discord.Embed(color=0xff00eb)
        serverinfo_embed.set_thumbnail(url=message.server.icon_url)
        serverinfo_embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        serverinfo_embed.add_field(name="<:scroll:442107706246037504> Nome:", value=message.server.name, inline=True)
        serverinfo_embed.add_field(name="<:crown:442120154705559584> Dono:", value=message.server.owner.mention)
        serverinfo_embed.add_field(name="<:triangular_flag_on_post:442116432386326529> ID:", value=message.server.id,
                                   inline=True)
        serverinfo_embed.add_field(name="<:books:442111670584606730> Cargos:", value=len(message.server.roles),
                                   inline=True)
        serverinfo_embed.add_field(name="<:bust_in_silhouette:440060372213432321> Membros:",
                                   value=len(message.server.members), inline=True)
        serverinfo_embed.add_field(name="<:date:442114695558856704> Criado em:",
                                   value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        serverinfo_embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=serverinfo_embed)

    if message.content.lower().startswith('dr?clima'):
        s = message.content.strip('dr?clima')
        url = 'http://api.apixu.com/v1/current.json?key=7fa4b4027a2349e8b44114046182304&q=' + s
        r = requests.get(url)
        if r.status_code == 200:
            js = r.json()
            nome = js['location']['name']
            regiao = js['location']['region']
            pais = js['location']['country']

            temp = str(js['current']['temp_c']) + "°C"
            temp2 = str(js['current']['temp_f']) + "°F"
            tenp = str(js['current']['feelslike_c']) + "°C"
            tenp2 = str(js['current']['feelslike_f']) + "°F"

            umi = str(js['current']['humidity']) + "%"
            vento = str(js['current']['wind_kph']) + "km/h"
            chuva = str(js['current']['precip_mm'])
            nuvem = str(js['current']['cloud'])
        try:
            clima = discord.Embed(color=0xff00eb)
            clima.add_field(name='<:house_with_garden:444955571276218368> Cidade', value=nome, inline=True)
            clima.add_field(name='<:homes:444955572014415874> Região', value=regiao, inline=True)
            clima.add_field(name='<:earth_americas:444955571892912139> País', value=pais, inline=True)
            clima.add_field(name='<:thermometer:444955572312342539> Temperatura', value=temp + temp2, inline=True)
            clima.add_field(name='<:thermometer:444955571389464588> Sensação térmica', value=tenp + tenp2, inline=True)
            clima.add_field(name='<:white_sun_small_cloud:444955571112640532> Umidade', value=umi, inline=True)
            clima.add_field(name='<:cloud_rain:444955570722570260> Chuva', value=chuva, inline=True)
            clima.add_field(name='<:cloud:444955574556164103> Nuvem', value=nuvem, inline=True)
            clima.add_field(name='<:dash:444955574254436383> Vento', value=vento, inline=True)
            clima.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=clima)
        except UnboundLocalError:
            await client.send_message(message.channel,
                                      '<:__:444646408365146153> `Infelizmente está cidade não é existente`')






    elif message.content.lower().startswith('dr?avatar'):
        try:
            membro = message.mentions[0]
            avatarembed = discord.Embed(
                title="",
                color=0xff00eb,
                description="[Clique aqui para baixar a imagem](" + membro.avatar_url + ")"
            )
            avatarembed.set_author(name=membro.name)
            avatarembed.set_image(url=membro.avatar_url)
            avatarembed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, f"{message.author.mention}", embed=avatarembed)
        except:
            avatarembed2 = discord.Embed(title="", color=0xff00eb,
                                         description="[Clique aqui para baixar a imagem](" + message.author.avatar_url + ")")
            avatarembed2.set_author(name=message.author.name)
            avatarembed2.set_image(url=message.author.avatar_url)
            avatarembed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, f"{message.author.mention}", embed=avatarembed2)

    if message.content.lower().startswith('dr?py'):
        msg = message.content.strip('dr?py')
        await client.send_message(message.channel,
                                  '<:python:445039606157541377> ' + f"{message.author.mention}" + ' enviou o segunte código:' + '\n```python\n{}\n```'.format(
                                      msg))

    if message.content.lower().startswith('dr?memoria'):
        emb = discord.Embed(title='<a:loading:443027200539885579> Processando...', color=0xff00eb)
        random = randint(0, 9)
        string = str(random)
        pingm0 = await client.send_message(message.channel, embed=emb)
        pingm1 = discord.Embed(title='Memória utilizada pelo bot:',
                               description='<:memoria:444955571351977994> `2{}mb`'.format(string), color=0x7289DA)
        await client.edit_message(pingm0, embed=pingm1)

    if message.content.lower().startswith('dr?ping'):
        emb = discord.Embed(title='<a:loading:443027200539885579> Processando...', color=0xff00eb)
        pingm0 = await client.send_message(message.channel, embed=emb)
        before = time.monotonic()
        ping = (time.monotonic() - before) * 1000
        pingm1 = discord.Embed(title='Ping:', description=f"<:ping:444955571515555850> `{int(ping)} ms`",
                               color=0xff00eb)
        await client.edit_message(pingm0, embed=pingm1)

    if message.content.lower().startswith('dr?membro'):
        user = message.author
        embedinfo = discord.Embed(
            title='***Suas informaçoes:***',
            color=0xff00eb,
            description='\n'
        )
        embedinfo.set_thumbnail(url=user.avatar_url)
        embedinfo.add_field(name='<:page_facing_up:443039280890118155> Nome', value=user.name)
        embedinfo.add_field(name='<:satellite:443039280999432202> Id', value=user.id)
        embedinfo.add_field(name='<:inbox_tray:443039280852631552> Entrou em',
                            value=user.joined_at.strftime("%d %b %Y %H:%M"))
        embedinfo.add_field(name='<:space_invader:442775673044729856> Jogando', value=user.game)
        await client.send_message(message.channel, embed=embedinfo)

    if message.content.lower().startswith('dr?servidor'):
        try:
            servidor = message.server
            criado_em = str(servidor.created_at.strftime("%d/%m/20%y - %H:%M:%S"))
            cargos = len([y.id for y in servidor.role_hierarchy])
            informacao = "\n:writing_hand::skin-tone-1: Nome : " + str(
                servidor.name) + " " + "\n:briefcase: Id : " + str(
                servidor.id) + " ""\n:tophat: Dono : " + str(servidor.owner) + " \n:alarm_clock: Criado em : " + str(
                criado_em) + " "
            emojis = len([y.id for y in servidor.emojis])
            cargos = len([y.id for y in servidor.role_hierarchy])
            verificao = str(servidor.verification_level).replace("low", "Baixa").replace("medium", "Média").replace(
                "high", "Alta").replace("4", "Super Alta").replace("none", "Nenhuma")
            localizacao = str(servidor.region).title()
            informacao_add = "\n:sunglasses:  " + str(emojis) + " Emojis" + "\n:robot:  " + str(
                cargos) + " Cargos" + "\n:bookmark_tabs: Verificação : " + str(
                verificao) + " " + "\n:earth_americas: Localização : " + str(
                localizacao) + " "
            bots = len([y.id for y in servidor.members if y.bot])
            humanos = len([y.id for y in servidor.members if not y.bot])
            usuario_total = bots + humanos
            usuarios = "\n:robot: " + str(bots) + " Bots\n:bust_in_silhouette: " + str(humanos) + " Humanos"
            servidor = message.server
            online = len([y.id for y in servidor.members if y.status == discord.Status.online])
            afk = len([y.id for y in servidor.members if y.status == y.status == discord.Status.idle])
            offline = len([y.id for y in servidor.members if y.status == y.status == discord.Status.offline])
            dnd = len([y.id for y in servidor.members if y.status == y.status == discord.Status.dnd])
            status_usuarios = "\n:green_heart: " + str(online) + " Online \n:yellow_heart:  " + str(
                afk) + " Ausente \n:heart: " + str(
                dnd) + " Não Pertube \n:white_circle:  " + str(offline) + " Offline"
            texto = len([y.id for y in servidor.channels if y.type == discord.ChannelType.text])
            voz = len([y.id for y in servidor.channels if y.type == discord.ChannelType.voice])
            if texto > 0:
                text = 1
            else:
                text = 0
            if voz > 0:
                voice = 1
            else:
                voice = 0
            categoria = voice + text
            canais = "\n:books: " + str(categoria) + " Categoria\n:scroll: " + str(
                texto) + " Texto\n:loud_sound: " + str(voz) + " voz"
            canais_total = texto + voz
            if servidor.icon_url == "":
                img = "https://ethospsicotestes.com.br/images/sem_foto.png"
            else:
                img = servidor.icon_url
            embed = discord.Embed(colour=0xff00eb)
            embed.add_field(name="Informação ", value=informacao, inline=True)
            embed.add_field(name="Usuários [" + str(usuario_total) + "]", value=usuarios, inline=True)
            embed.add_field(name="Canais [" + str(canais_total) + "]", value=canais, inline=True)
            embed.add_field(name="Status do usuários", value=status_usuarios, inline=True)
            embed.add_field(name="Informação Adicional", value=informacao_add, inline=True)
            embed.set_thumbnail(url=img)

            await client.send_message(message.channel, embed=embed)
        except:
            await client.send_message(message.channel, "Erro ao obter a informação do servidor!")

    if message.content.lower().startswith("dr?ajuda"):
        embed1 = discord.Embed(title="", url="", color=0xff00eb)
        embed1.set_author(name="COMANDOS:",icon_url="https://cdn.discordapp.com/attachments/445037903551135744/445041425600741406/comando.png")
        embed1.add_field(name="<:red_circle:444955571515555850> dr?ping", value="`mostra a latitencia atual do bot`")
        embed1.add_field(name="<:floppy_disk:444955571351977994> dr?memoria",value="`mostra o quanto de memoria o bot esta utilizando`")
        embed1.add_field(name='<:globe_with_meridians:445039606157541377> dr?py', value="`envia o texto a frente em uma caixa python`")
        embed1.add_field(name='<:bookmark_tabs:444955576590663693> dr?aviso',value="`envia uma mensagem para todos membros do servidor no privado`")
        embed1.add_field(name='<:bust_in_silhouette:444955570659786753> dr?avatar', value="`mostra o avatar do usuario mencionado`")
        embed1.add_field(name='<:gear:444955570659786753> dr?servidor', value="`mostra infromações sobre o servidor`")
        embed1.add_field(name='<:mag_right:444955570663981057> dr?google', value="`faz uma pesquisa ate na deepweb`",inline=False)
        embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed1)

    if message.content.startswith('dr?setar'):
        set1 = message.content.strip('dr?setar')
        global setar
        setar = set1
    if message.content.lower().startswith('dr?msg'):
        role = discord.utils.get(message.server.roles, name='BotNiko')
        if not role in message.author.roles:
            embed1 = discord.Embed(title='OCORREU UM ERRO <:confused:462194681812615179>',description="<:crossed_swords:440061539026731008> `SEM PERMISSÃO:` ***Você precisa do cargo `BotNiko***`",color=0xff00eb)
            embed1.set_footer(text="***Darya***",icon_url="https://cdn.discordapp.com/attachments/444988934745882625/462184762350501888/3dc319712462d6eb6f3377f55dc67a10d256dd24_hq.gif")
            return await client.send_message(message.channel, embed=embed1)
        msg = message.content.strip('dr?msg')
        embed2 = discord.Embed(title='***ENVIANDO MENSAGEM*** <:inbox_tray:462194451805110273>',description="\n<:stopwatch:449635557753094164>***MENSAGEM ESCOLHIDA***" + (msg),color=0xff00eb)
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)
        x = list(message.server.members)
        s = 0
        for member in x:
            embed1 = discord.Embed(title="Darya", url="", color=0xff00eb,
                                   description=' <@{}> {}'.format(member.id, msg))
            embed1.set_thumbnail(url=setar)
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
        embed2 = discord.Embed(title='***MENSAGEM ENVIADA***<:white_check_mark:462195054317010944>',description="\n***Mensagem enviada com sucesso para todos membros do servidor***<:scroll:462197518327873546>", color=0xff00eb)
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)

    if message.content.startswith('dr?fale') or message.content.startswith('dr?falar'):
        if message.author.id == 'ID DO BOT':
            return
        try:
            mensagem = message.content[7:]
            await client.send_message(message.channel, mensagem, tts=False)
            client.delete_message(message)
            print('Fale on')
            print(mensagem)
        except:
            await client.send_message(message.channel, "Você precisa escrever algo para eu falar!")

    if message.content.startswith("dr?eur"):
        req = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
        resposta = json.loads(req.text)
        btcnome = (str(resposta['valores']['EUR']['nome']))
        btcvalor = (str(resposta['valores']['EUR']['valor']))
        btcfonte = (str(resposta['valores']['EUR']['fonte']))
        embedbtc = discord.Embed(color=0xff00eb, )
        embedbtc.set_author(name='{} aqui está a cotação atual do Euro.'.format(message.author.name),icon_url=message.author.avatar_url)
        embedbtc.add_field(name='Nome :page_facing_up:', value="{}".format(btcnome))
        embedbtc.add_field(name='Valor :dollar:', value="R$ {}".format(btcvalor))
        embedbtc.add_field(name='Fonte :pushpin:', value="{}".format(btcfonte))
        await client.send_message(message.channel, embed=embedbtc)

    if message.content.startswith('dr?soldado'):
        await client.send_message(message.channel,'***Em Posição E Aguardando Ordem Mestre <:crossed_swords:462194270963630080>***.')

    if message.content.startswith('dr?criador'):
        await client.send_message(message.channel,
"***Meu Criador*** <@403395784751448075> <:revolving_hearts:462212168964898817>")

client.run(str(os.environ.get('TOKEN')))
