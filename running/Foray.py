from dotenv import load_dotenv
from dataStructures import Game, Telegram
from telethon.sync import TelegramClient, events
import re, asyncio, random, os, sys



# Importa las variables de la api desde el archivo .env
load_dotenv ()
api_id = os.getenv ("API_ID")
api_hash = os.getenv ("API_HASH")

# Importa las variables de uso desde el archivo de Telegram
cw = Telegram.cw_tag

# Importa las variables de uso desde el archivo de Game
reg_stroll = re.compile (Game.foray_text)



print ("Trying to connect telegram")
with TelegramClient ("Tachiri", int (api_id), api_hash) as client:
    print ("Connected to telegram")
    client.send_message ('me', "Online")


    @client.on (events.NewMessage (chats = cw, incoming = True) )
    async def chatwars_handler (foray_event):
        if re.search (reg_stroll, foray_event.raw_text):
            sleep_time = random.randint (8, 90)

            await asyncio.sleep (sleep_time)
            await foray_event.click (0)


    client.run_until_disconnected ()