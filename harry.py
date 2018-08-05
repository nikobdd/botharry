import discord
import os


client = discord.Client()
@client.event
async def on_ready():
    print("------------?  S P E C T R U M  ?-------------")
    print("Servidores: {} Serves".format(str(len(client.servers))))
    print("------------?  S P E C T R U M  ?-------------")
    await client.change_presence(game=discord.Game(name=',ajuda', type=1, url='https://www.twitch.tv/eabot'),status='streaming')

@client.event
async def on_message(message):
    if message.content.lower ().startswith ( "harry,ban" ):
        try:

            if not message.author.server_permissions.ban_members:
                return await client.send_message ( message.channel,' <:fire:457629062064635905>️Permissão Insuficiente' )
            author = message.author.mention
            user = message.mentions[0]
            embed1 = discord.Embed ( color=0xff0101)
            embed1.set_footer ( text=client.user.name, icon_url=client.user.avatar_url )
            embed1.set_image (url="https://d2118lkw40i39g.cloudfront.net/wp-content/uploads/2016/09/harry-potter-dementor-giphy.gif" )
            await client.ban ( user )
            embed1.add_field (name="***✠ SPECTRUM ✠***",value='{}***Foi Banido Com Sucesso Senhor*** **{}**'.format ( user.mention, author ) )
            embed1.set_image (url="https://d2118lkw40i39g.cloudfront.net/wp-content/uploads/2016/09/harry-potter-dementor-giphy.gif" )
            embed1.set_footer (text=client.user.name, icon_url=client.user.avatar_url )
            await client.send_message ( message.channel, embed=embed1 )
        except discord.errors.Forbidden:
            return await client.send_message ( message.channel,'<:crossed_swords:457638598607503360> **|** ***Infelizmente o cargo do usuario mencionado e maior que o meu , ou ele é um administrador***.' )



    if message.content.startswith(',setar'):
        set1 = message.content.strip(',setar')
        global setar
        setar = set1

    if message.content.lower().startswith(',msg'):
        msg = message.content.strip(',msg')
        embed2 = discord.Embed(title='ENVIANDO MENSAGEM...',description='<:conometro:449635557753094164> `MENSAGEM ESCOLHIDA:`\n' + (msg),color=0xff0101)
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)
        x = list(message.server.members)
        s = 0
        for member in x:
            embed1 = discord.Embed(title="Aviso Do Servidor: ✠ S P E C T R U M  ✠", url="", color=0xff0101,description=' <@{}> {}'.format(member.id, msg))
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
        
        
        
    if not (not message.content.startswith ( '.fale' ) and not message.content.startswith ( '.falar' )):
        if message.author.id == 'ID DO BOT':
            return
        try:
            mensagem = message.content[7:]
            await client.delete_message ( message )
            await client.send_message ( message.channel, mensagem, tts=False )
            print ( 'Fale on' )
            print ( mensagem )
        except:
            await client.send_message ( message.channel, "Você precisa escrever algo para eu falar!" )        
        
        
        
    if message.content.startswith ( '.membros' ):
        # Importar time e datetime
        user = message.author.name
        horario = datetime.datetime.now ().strftime ( "%H:%M:%S" )
        membros_embed = discord.Embed ( title="\n",description="***Quantidade De Membros No Servidor! :inbox_tray: ***",color=0x5c02db )
        membros_embed.set_thumbnail ( url=message.server.icon_url )
        membros_embed.set_footer ( text="Comando requisitado por {} • Hoje às {}".format ( user, horario ) )
        membros_embed.add_field ( name="Membros no servidor:***", value=len ( message.server.members ), inline=True )
        await client.send_message ( message.channel, embed=membros_embed )
        
        
        
     if message.content.lower ().startswith ( '.py' ):
        msg = message.content.strip ( '.py' )
        await client.delete_message ( message )
        await client.send_message ( message.channel,'<:rotating_light:474586348716556319> ' + ' ***Sistema De Monitoramento  ✠ S P E C T R U M  ✠***:' + '\n```python\n{}\n```'.format (msg ) )
       
        
        
        
        
    if message.content.startswith ( '.uptime' ):
        await client.send_message ( message.channel,"***Estou online a {0} hora(s) e {1} minuto(s)***".format ( hour, minutes ) )

    async def tutorial_uptime():
        await client.wait_until_ready ()
        global minutes
        minutes = 0
        global hour
        hour = 0
        while not client.is_closed:
            await asyncio.sleep ( 60 )
            minutes += 1
            if minutes == 60:
                minutes = 0
                hour += 1

    client.loop.create_task ( tutorial_uptime () )        
        
        
        
 @client.event
async def on_member_join(member):
    role1 = "♰ 𝑀𝐸𝑀𝐵𝐸𝑅𝒮 ♰"
    role = discord.utils.find ( lambda r: r.name == "{}".format ( role1 ), member.server.roles )
    await client.add_roles ( member, role )
    embedvindo = discord.Embed ( color=0x5c02db, title='***🎈 Sejá Bem Vindo (a)***',description='✨' + member.mention + ' ***ao  ✠  S P E C T R U M  ✠  Esperamos Que Se Divitar  🎆 🎊***' )
    embedvindo.set_thumbnail ( url=member.avatar_url )
    embedvindo.set_author ( name=member.name, icon_url=member.avatar_url )
    mensagemvindo2 = "💬-chat-livre"
    bemvindo = discord.utils.find ( lambda c: c.name == "{}".format ( mensagemvindo2 ), member.server.channels )
    await client.send_message ( bemvindo, embed=embedvindo )           
       

client.run(str(os.environ.get('TOKEN')))
