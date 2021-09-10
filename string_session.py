from telethon.sessions import StringSession
from telethon.sync import TelegramClient

logo = """
 ____   ___  ____ _____ ____  _____ _   _ ____  _____ ____  
|  _ \ / _ \/ ___|_   _/ ___|| ____| \ | |  _ \| ____|  _ \ 
| |_) | | | \___ \ | | \___ \|  _| |  \| | | | |  _| | |_) |
|  __/| |_| |___) || |  ___) | |___| |\  | |_| | |___|  _ < 
|_|    \___/|____/ |_| |____/|_____|_| \_|____/|_____|_| \_\
                                                            

"""
baap_bolte = """
#POSET  Sender
Made With Love By AK
"""
                                                                                                            
print("")
print(logo)
print("""Kindly Enter Your Details To Continue ! """)

API_ID = int(input("API_ID: "))
API_HASH = input("API_HASH: ")

while True:
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as client:
            print("String Sent To Your Saved Message, Store It To A Safe Place!! ")
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n",
            )
            break
    except Exception as error:
        print(error)
        print(
            "Wrong phone number \n make sure its with correct country code. Example : +919961998999 ! Kindly Retry"
        )
        print("")
        break
