import discord
import datetime
import json
client = discord.Client()

contador = {'000000000000000000': {'serverid': '000000000000000000', 'canalid': '000000000000000000', 'conta-at': 0}}
texto = {'000000000000000000': {'serverid': '000000000000000000', 'texto': '000000000000000000'}}

@client.event
async def on_ready():
    print('CONTADOR=ON')

@client.event
async def on_message(message):
    if message.content.startswith('t!contador'):
     if message.author.server_permissions.administrator:
        with open('contador.json', 'r') as f:
            contador = json.load(f)
        with open('texto.json', 'r') as f:
            texto = json.load(f)
        if message.server.id in contador:
            pass
        else:
            contador[message.server.id] = {'conta-at': 1}
        set1 = message.content[11:]
        if '{}'.format(set1) == 'on':
         await client.send_message(message.channel, '<:EmoteConfig:486869372162539520> O canal {} foi definido com sucesso! <:switchON:487455703112613919>'.format(message.channel.mention))
         if message.server.id in texto:
          numeros = str(len(message.server.members)).replace("0", "setar-zero").replace("1", "setar-um").replace("2","setar-dois").replace("3", "setar-tres").replace("4", "setar-quatro").replace("5", "setar-cinco").replace("6","setar-seis").replace("7", "setar-sete").replace("8", "setar-oito").replace("9", "setar-nove")
          await client.edit_channel(message.channel, topic="<a:Bouncycat:528337139155599360> Membros: " + str(numeros).replace("setar-zero","<:00V:528673420582322186>").replace("setar-um", "<:01V:528673424420241418>").replace("setar-dois","<:02V:528673427020709888>").replace("setar-tres", "<:03V:528673426454478868>").replace("setar-quatro", "<:04V:528673426404147203>").replace("setar-cinco", "<:05V:528673426483707905>").replace("setar-seis","<:06V:528673425628332033>").replace("setar-sete", "<:07V:528673425628069910>").replace("setar-oito","<:08V:528673426462998529>").replace("setar-nove", "<:09V:528673426966183946>") + ' {}'.format(str(texto[message.server.id]['texto'])))
          contador[message.server.id] = {'serverid': '{}'.format(message.server.id), 'canalid': '{}'.format(message.channel.id), 'conta-at': 0}
         else:
          numeros = str(len(message.server.members)).replace("0", "setar-zero").replace("1", "setar-um").replace("2","setar-dois").replace("3", "setar-tres").replace("4", "setar-quatro").replace("5", "setar-cinco").replace("6","setar-seis").replace("7", "setar-sete").replace("8", "setar-oito").replace("9", "setar-nove")
          await client.edit_channel(message.channel, topic="<a:Bouncycat:528337139155599360> Membros: " + str(numeros).replace("setar-zero", "<:00V:528673420582322186>").replace("setar-um","<:01V:528673424420241418>").replace("setar-dois", "<:02V:528673427020709888>").replace("setar-tres","<:03V:528673426454478868>").replace("setar-quatro", "<:04V:528673426404147203>").replace("setar-cinco","<:05V:528673426483707905>").replace("setar-seis", "<:06V:528673425628332033>").replace("setar-sete","<:07V:528673425628069910>").replace("setar-oito", "<:08V:528673426462998529>").replace("setar-nove","<:09V:528673426966183946>"))
          contador[message.server.id] = {'serverid': '{}'.format(message.server.id),'canalid': '{}'.format(message.channel.id), 'conta-at': 0}
        if '{}'.format(set1) == 'off':
         if contador[message.server.id]['conta-at'] == 0:
          iddocanal = "{}".format(str(contador[message.server.id]['canalid']))
          canaleditar = client.get_channel(iddocanal)
          await client.send_message(message.channel, '<:EmoteConfig:486869372162539520> Você removeu as definições do contador! <:switchOFF:486869487610757120>')
          contador[message.server.id] = {'conta-at': 1}
          await client.edit_channel(canaleditar, topic=" ")
         else:
          await client.send_message(message.channel, '<:EmoteConfig:486869372162539520> Você precisa definir o contador antes de remover as definições.')

        if '{}'.format(set1) == '':
         embed = discord.Embed(description="Olá senhor(a) **{}**, Seja bem vindo(a) ao painel de configurações, aqui você pode modificar algumas configurações do seu contador.".format(message.author.name), color=0xe081e4)
         embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
         if contador[message.server.id]['conta-at'] == 0:
          iddocanal = "{}".format(str(contador[message.server.id]['canalid']))
          canaleditar = client.get_channel(iddocanal)
          embed.add_field(name='[On] = Define o canal do contador:', value='<:switchON:487455703112613919> Configuração definida\n**Canal:** {}\n**Para desativar:**```md\n* dpcontador off\n```'.format(canaleditar.mention))
         else:
          embed.add_field(name='[Off] = Define o canal do contador:', value='<:switchOFF:486869487610757120> Configuração não definida |** Para definir:**```md\n* dpcontador on\n```')
         if message.server.id in texto:
          embed.add_field(name='[Editar] = Define o texto do contador:', value='<:switchON:487455703112613919> Configuração definida |\n**Texto:** {}\n**Para editar:**  ```md\n* dpcontador editar > texto\n```'.format(str(texto[message.server.id]['texto'])))
         else:
          embed.add_field(name='[Editar] = Define o texto do contador:', value='<:switchOFF:486869487610757120> Configuração não definida |** Para definir:**  ```md\n* dpcontador editar > texto \n```')
         embed.set_thumbnail(url="https://cdn.discordapp.com/icons/522914004251836417/82941e6e16b0b1166db1c0ffb4c0ef9f.jpg?size=2048")
         embed.set_footer(text=message.server.name, icon_url=message.server.icon_url)
         embed.timestamp = datetime.datetime.utcnow()
         return await client.send_message(message.channel, embed=embed)
        with open('contador.json', 'w') as f:
            json.dump(contador, f)
        with open('texto.json', 'w') as f:
            json.dump(texto, f)
     else:
        await client.send_message(message.channel, '<:stop:485944474703233034> Você precisa ser um administrador.')
    if message.content.startswith('t!contador editar'):
     if message.author.server_permissions.administrator:
        with open('contador.json', 'r') as f:
            contador = json.load(f)
        with open('texto.json', 'r') as f:
            texto = json.load(f)
        set1 = message.content[18:]
        texto[message.server.id] = {'serverid': message.server.id, 'texto': set1}
        if '{}'.format(set1) == '':
         await client.send_message(message.channel, '<:EmoteConfig:486869372162539520> **Você precisa colocar um texto para definir.**')
        else:
         if contador[message.server.id]['conta-at'] == 0:
          iddocanal = "{}".format(str(contador[message.server.id]['canalid']))
          canaleditar = client.get_channel(iddocanal)
          numeros = str(len(message.server.members)).replace("0", "setar-zero").replace("1", "setar-um").replace("2","setar-dois").replace("3", "setar-tres").replace("4", "setar-quatro").replace("5", "setar-cinco").replace("6","setar-seis").replace("7", "setar-sete").replace("8", "setar-oito").replace("9", "setar-nove")
          await client.edit_channel(message.channel, topic="<a:picafeliz:489822390151282693> Membros: " + str(numeros).replace("setar-zero","<:00V:528673420582322186>").replace("setar-um", "<:01V:528673424420241418>").replace("setar-dois","<:02V:528673427020709888>").replace("setar-tres", "<:03V:528673426454478868>").replace("setar-quatro", "<:04V:528673426404147203>").replace("setar-cinco", "<:05V:528673426483707905>").replace("setar-seis","<:06V:528673425628332033>").replace("setar-sete", "<:07V:528673425628069910>").replace("setar-oito","<:08V:528673426462998529>").replace("setar-nove", "<:09V:528673426966183946>") + ' {}'.format(str(texto[message.server.id]['texto'])))
          await client.send_message(canaleditar, '<:EmoteConfig:486869372162539520> Você definiu o texto do contador!\n<:EmoteChannel:485919232924844033>**Texto:** {}'.format(set1))
         else:
          await client.send_message(message.channel, '<:EmoteConfig:486869372162539520> Você definiu o texto do contador!\n<:EmoteChannel:485919232924844033>**Texto:** {}'.format(set1))
        with open('contador.json', 'w') as f:
            json.dump(contador, f)
        with open('texto.json', 'w') as f:
            json.dump(texto, f)
     else:
      await client.send_message(message.channel, '<:stop:485944474703233034> Você precisa ser um administrador.')
@client.event
async def on_member_join(member):
    with open('contador.json', 'r') as f:
      contador = json.load(f)
    with open('texto.json', 'r') as f:
      texto = json.load(f)
    servidor = member.server
    id = servidor.id
    if servidor.id in contador:
     if servidor.id == id:
      if servidor.id in texto:
       if contador[id]['conta-at'] == 0:
        iddocanal = "{}".format(str(contador[id]['canalid']))
        canaleditar = client.get_channel(iddocanal)
        numeros = str(len(servidor.members)).replace("0", "setar-zero").replace("1", "setar-um").replace("2", "setar-dois").replace("3", "setar-tres").replace("4", "setar-quatro").replace("5", "setar-cinco").replace("6", "setar-seis").replace("7", "setar-sete").replace("8", "setar-oito").replace("9", "setar-nove")
        await client.edit_channel(canaleditar, topic="<a:Bouncycat:528337139155599360> Membros: " + str(numeros).replace("setar-zero","<:zero:485136919186112512>").replace("setar-um", "<:um:485136919144169472>").replace("setar-dois","<:dois:485136914069061632>").replace("setar-tres", "<:tres:485136919110483994>").replace("setar-quatro", "<:quatro:485136913968136192>").replace("setar-cinco", "<:cinco:485136914144559104>").replace("setar-seis", "<:seis:485136913896833026>").replace("setar-sete", "<:Sete:485136918649110539>").replace("setar-oito", "<:oito:485136914047959040>").replace("setar-nove", "<:nove:485136913934843915>") + ' {}'.format(str(texto[id]['texto'])))
      else:
       if contador[id]['conta-at'] == 0:
        iddocanal = "{}".format(str(contador[id]['canalid']))
        canaleditar = client.get_channel(iddocanal)
        numeros = str(len(servidor.members)).replace("0", "setar-zero").replace("1", "setar-um").replace("2", "setar-dois").replace("3", "setar-tres").replace("4", "setar-quatro").replace("5", "setar-cinco").replace("6", "setar-seis").replace("7", "setar-sete").replace("8", "setar-oito").replace("9", "setar-nove")
        await client.edit_channel(canaleditar, topic="<a:Bouncycat:528337139155599360> Membros: " + str(numeros).replace("setar-zero","<:00V:528673420582322186>").replace("setar-um", "<:01V:528673424420241418>").replace("setar-dois","<:02V:528673427020709888>").replace("setar-tres", "<:03V:528673426454478868>").replace("setar-quatro", "<:04V:528673426404147203>").replace("setar-cinco", "<:05V:528673426483707905>").replace("setar-seis", "<:06V:528673425628332033>").replace("setar-sete", "<:07V:528673425628069910>").replace("setar-oito", "<:08V:528673426462998529>").replace("setar-nove", "<:09V:528673426966183946>"))
@client.event
async def on_member_remove(member):
    with open('contador.json', 'r') as f:
      contador = json.load(f)
    with open('texto.json', 'r') as f:
      texto = json.load(f)
    servidor = member.server
    id = servidor.id
    if servidor.id in contador:
     if servidor.id == id:
      if servidor.id in texto:
       if contador[id]['conta-at'] == 0:
        iddocanal = "{}".format(str(contador[id]['canalid']))
        canaleditar = client.get_channel(iddocanal)
        numeros = str(len(servidor.members)).replace("0", "setar-zero").replace("1", "setar-um").replace("2", "setar-dois").replace("3", "setar-tres").replace("4", "setar-quatro").replace("5", "setar-cinco").replace("6", "setar-seis").replace("7", "setar-sete").replace("8", "setar-oito").replace("9", "setar-nove")
        await client.edit_channel(message.channel, topic="<a:Bouncycat:528337139155599360> Membros: " + str(numeros).replace("setar-zero","<:00V:528673420582322186>").replace("setar-um", "<:01V:528673424420241418>").replace("setar-dois","<:02V:528673427020709888>").replace("setar-tres", "<:03V:528673426454478868>").replace("setar-quatro", "<:04V:528673426404147203>").replace("setar-cinco", "<:05V:528673426483707905>").replace("setar-seis","<:06V:528673425628332033>").replace("setar-sete", "<:07V:528673425628069910>").replace("setar-oito","<:08V:528673426462998529>").replace("setar-nove", "<:09V:528673426966183946>") + ' {}'.format(str(texto[message.server.id]['texto'])))
      else:
       if contador[id]['conta-at'] == 0:
        iddocanal = "{}".format(str(contador[id]['canalid']))
        canaleditar = client.get_channel(iddocanal)
        numeros = str(len(servidor.members)).replace("0", "setar-zero").replace("1", "setar-um").replace("2", "setar-dois").replace("3", "setar-tres").replace("4", "setar-quatro").replace("5", "setar-cinco").replace("6", "setar-seis").replace("7", "setar-sete").replace("8", "setar-oito").replace("9", "setar-nove")
        await client.edit_channel(canaleditar, topic="<a:Bouncycat:528337139155599360> Membros: " + str(numeros).replace("setar-zero","<:00V:528673420582322186>").replace("setar-um", "<:01V:528673424420241418>").replace("setar-dois","<:02V:528673427020709888>").replace("setar-tres", "<:03V:528673426454478868>").replace("setar-quatro", "<:04V:528673426404147203>").replace("setar-cinco", "<:05V:528673426483707905>").replace("setar-seis", "<:06V:528673425628332033>").replace("setar-sete", "<:07V:528673425628069910>").replace("setar-oito", "<:08V:528673426462998529>").replace("setar-nove", "<:09V:528673426966183946>"))

        
        
client.run(str(os.environ.get('TOKEN')))
