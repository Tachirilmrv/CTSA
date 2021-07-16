from dotenv import load_dotenv
from dataStructures import Game, Telegram
from telethon.sync import TelegramClient, events
import re, asyncio, os



# Importa las variables de la api desde el archivo .env
load_dotenv (dotenv_path = ".idea/.env")
api_id = os.getenv ("API_ID")
api_hash = os.getenv ("API_HASH")


autocraft = 84
cw = "@chtwrsbot"
global ress
wel = re.compile('Welcome, to the ')

print('Trying to connect telegram')
with TelegramClient("untao", api_id, api_hash) as client:
    print("Connected to telegram")

    client.send_message(cw, "/ws_")


    @client.on(events.NewMessage(chats=cw, incoming=True))
    async def welcome(event):
        if re.search(wel, event.raw_text):
            await client.forward_messages(autocraft, event.message)


    @client.on(events.NewMessage(chats=cw, incoming=True))
    async def nomana(event):
        if "Not enough mana" in event.raw_text:
            await client.forward_messages(autocraft, event.message)


    @client.on(events.NewMessage(chats=autocraft, incoming=True))
    async def craftRequest(event):
        if "/c_" in event.raw_text:
            global ress
            ress = re.findall("(?<=/c_)\d+", event.raw_text)

            await client.forward_messages(cw, event.message)


    @client.on(events.NewMessage(chats=cw, incoming=True))
    async def notEnough(event):
        if "Not enough materials" in event.raw_text:
            await client.forward_messages(autocraft, event.message)


    @client.on(events.NewMessage(chats=autocraft, incoming=True))
    async def receive(event):
        if "/g_receive" in event.raw_text:
            await client.forward_messages(cw, event.message)


    @client.on(events.NewMessage(chats=cw, incoming=True))
    async def crafted(event):
        global ress
        if "Crafted:" in event.raw_text:
            quantity = re.findall("\d+", event.raw_text)
            final_quantity = 0

            for i in quantity:
                final_quantity += int(i)

            await asyncio.sleep(2)
            await client.send_message(cw, "/g_deposit {} {}".format(ress[0], final_quantity))


    @client.on(events.NewMessage(chats=cw, incoming=True))
    async def deposited(event):
        if "Deposited successfully" in event.raw_text:
            await client.forward_messages(autocraft, event.message)


    client.run_until_disconnected()
