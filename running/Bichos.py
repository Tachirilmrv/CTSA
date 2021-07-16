from dotenv import load_dotenv
from dataStructures import Game, Telegram
from telethon.sync import TelegramClient, events
import re, asyncio, random, os



# Importa las variables de la api desde el archivo .env
load_dotenv (dotenv_path = ".idea/.env")
api_id = os.getenv ("API_ID")
api_hash = os.getenv ("API_HASH")


reg_creatures = re.compile (Game.creatures_text)
reg_stroll = re.compile (Game.foray_text)

cw = Telegram.cw_tag
angryBirbs_bot = Telegram.angry_birbs_tag
hunt = Telegram.hunt_name
repair = 'repaired'
forge = Telegram.sky_forge_tag

print ("Trying to connect telegram")
with TelegramClient("untao", itn (api_id), api_hash) as client:
    print ("Connected to telegram")
    client.send_message ('me', "Bichos y repas must die")


    @client.on(events.NewMessage (chats = cw, incoming = True) )
    async def chatwars_handler (event):
        if re.search (reg_stroll, event.raw_text):
            sleep_time = random.randint (15, 45)
            await asyncio.sleep (sleep_time)
            await event.click (0)

        if re.search (repair, event.raw_text):
            await client.forward_messages (forge, event.message)


    @client.on (events.NewMessage (chats = angryBirbs_bot, incoming = True) )
    async def creatures_handler (event):
        await event.click (0)
        #	if re.search (re.compile('fight'), event.message):
        #        await asyncio.sleep (1)
        await client.forward_messages (cw, event.message)


    @client.on (events.NewMessage (chats = hunt, incoming = True) )
    async def bichos_handler (event):
        if re.search (reg_creatures, event.raw_text):
            await client.send_message (cw, event.raw_text)


    client.run_until_disconnected ()
