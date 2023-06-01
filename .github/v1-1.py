from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest
from telethon import types, utils, errors
import configparser
import sys
import os
import csv
from csv import reader
import traceback
import time
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from colorama import init, Fore
init()
n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]
def HackingZonepost():
    import random
    os.system('clear')
    print(f"""
    {cy}{ye}
    
 ____  _           _      _                 _   _       _
/ ___|| |__   ___ (_)_ __(_) ___  _ __     | \ | | ___ / |
\___ \| '_ \ / _ \| | '__| |/ _ \| '_ \    |  \| |/ _ \| |       ___) | | | | (_) | | |  | | (_) | | | |   | |\  | (_) | |
|____/|_| |_|\___/|_|_| _/ |\___/|_| |_|___|_| \_|\___/|_|
                       |__/           |_____|""")
    print(f'{ye}https://www.youtube.com/@Shoirjon_No1')
HackingZonepost()
with open('memory.csv', 'r') as hash_obj:
    csv_reader = reader(hash_obj)
    list_of_rows = list(csv_reader)  
    row_number = 1
    col_number = 1
    numdel = list_of_rows[row_number - 1][col_number - 1]
    
delta = int(numdel)
global nextdelta
nextdelta = delta+1

with open('phone.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)    
    row_number = delta
    col_number = 1
    value = list_of_rows[row_number - 1][col_number - 1]


    
api_id = int(15606699)
api_hash = str('3c99082fff6a24903c7825fe935d4f5c')
pphone = value

config = configparser.ConfigParser()
config.read("config.ini")
to_group = config['Shoirjon_official']['ToGroup']

SLEEP_TIME_2 = 100
def autos():
    
    channel_username = to_group
    phone = utils.parse_phone(pphone)
    client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
    
    client.connect()
    if not client.is_user_authorized():
        print(Style.BRIGHT + Fore.RED + 'Õzgartirish')
        client.send_code_request(phone)
        client.sign_in(phone, input    (Style.BRIGHT + Fore.GREEN + 'Telegramga yuborilgan kodni kiriting: '))
    
    
    user = client.get_me()
    if not user.last_name:
        LegendName = user.first_name
    else:
        LegendName = user.first_name +' '+user.last_name
    input_file = 'data.csv'
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['srno'] = row[0]
            user['username'] = row[1]
            user['id'] = int(row[2])
            #user['access_hash'] = int(row[3])
            user['name'] = row[3]
            users.append(user)

    with open('memory.csv', 'r') as hash_obj:
        csv_reader = reader(hash_obj)
        list_of_rows = list(csv_reader)  
        row_number = 1
        col_number = 2
        numnext = list_of_rows[row_number - 1][col_number - 1]
    
    startfrom = int(numnext)
    nextstart = startfrom+50
    
    with open('memory.csv', 'r') as hash_obj:
        csv_reader = reader(hash_obj)
        list_of_rows = list(csv_reader)  
        row_number = 1
        col_number = 3
        numend = list_of_rows[row_number - 1][col_number - 1]
    
    endto = int(numend)
    nextend = endto+50
        
    with open("memory.csv","w",encoding='UTF-8') as df:
        writer = csv.writer(df, delimiter=",", lineterminator="\n")
        writer.writerow([nextdelta,nextstart,nextend])

    for user in users:
        if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
            try:
                status = 'Shoirjon_official'
                if user['username'] == "":
                    print("foydalanuvchi nomi yöq, keyingisiga õtish")
                    continue
                    
                client(InviteToChannelRequest(channel_username,[user['username']]))
                status = Style.BRIGHT + Fore.GREEN + 'Bajarildi'
                
                print(Style.BRIGHT + Fore.YELLOW + "Iltimos kuting...")
                time.sleep(random.randrange(15,30))
                
            except UserPrivacyRestrictedError:
                status = Style.BRIGHT + Fore.RED + 'Foydalanuvchi Maxfiyligi cheklangan'
                time.sleep(random.randrange(3,5))
                            
            except UserAlreadyParticipantError:
                status = 'ALLAQACHON'
                print = "Allaqachon qo'shilgan"
                            
            except PeerFloodError as g:
                status = 'PeerFloodError'
                print(Style.BRIGHT + Fore.YELLOW + 'Skript tayyorlanmoqda, shuning uchun kuting...')
                time.sleep(random.randrange(60,90))
                           
            except ChatWriteForbiddenError as cwfe:
                client(JoinChannelRequest(channel_username))
                time.sleep(5)
                continue
                
            except errors.RPCError as e:
                status = e.__class__.__name__
            
            except Exception as d:
            	status = d
            	
            except:
                traceback.print_exc()
                print("Kutilmagan xato")
                continue
            channel_connect = client.get_entity(channel_username)
            channel_full_info = client(GetFullChannelRequest(channel=channel_connect))
            countt = int(channel_full_info.full_chat.participants_count)

            print(Style.BRIGHT + Fore.GREEN +f" {LegendName} {Style.BRIGHT+Fore.RESET} > Guruh azolari {(countt)}{Style. RESET_ALL} {Style.BRIGHT+Fore.CYAN}>> {user['name']} >> {status}")
        elif int(user['srno']) > int(endto):
            print(Style.BRIGHT + Fore.GREEN + "\nAzolar muvaffaqiyatli qõshildi!\n")
            print(Style.BRIGHT + Fore.YELLOW + 'Chiqish uchun Enter tugmasini bosing')
            stat = input()
            if stat == 1 :
                autos()
            else:
                quit()
             
autos()