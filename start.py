import time
from colorama import Fore, Style
import os
import webbrowser
import configparser


text0 = "           ●Iltimos, diqqat qiling!● \n\nUshbu skript muallifi taqdim etilgan xizmatlardan foydalanish natijasida yuzaga keladigan har qanday oqibatlar uchun javobgar emas. Barcha materiallar faqat ta'lim maqsadida nashr etilgan!\n\nDasturchi: SHOIRJON  MAMAZOKIROV\nMualliflik huquqi: T.me/Shoirjon_No1\n"

text1 = " Demak ishni boshlaymiz"
text2 = " <<<<<<<<<Nima qilishni tanlang>>>>>>>>>>"
text3 = "<1>  Kerakli asboblarni o'rnatish"
text4 = "<2>  Raqam qo'shish/o'chirish"
text5 = "<3>  Guruxni taxrirlash"
text6 = "<4>  Qo'shish_v3"
text7 = "<5>  Dastur xaqida qisqacha"
text8 = "<6>  Muammo xaqida xabar berish"
text9 = "<7>  Chiqish"
text10 = "    ●Dasturchi bilan Telegram orqali aloqa qilishingiz mumkun. Dastur xaqida har qanday muammoni va ozingizning taklifingizni berishingiz mumkun. \n\Shuningdek hamkorlik taklifi ham mavjud\n\nDasturchi bilan bog'lanish uchun <y> harifi bilan <Enter> bosing\n \nTelegram: https://t.me/Shoirjon_No1 "

lg = '\033[1;32;40m'
r = '\033[0m'
clr = lambda: os.system('clear')

def ornatish():
    os.system('clear')
    os.system('python setup.py')

    main_menu()

def b():
    os.system('clear')
    os.system('python csvtahrir.py')
    main_menu()

def c():
    os.system('clear')
    os.system('python initaxrir.py')
    main_menu()

def d():
    os.system('clear')
    os.system('python Telegram.py')
    main_menu()
def ebout():
    os.system('clear')
    os.system('python about.py')
    main_menu()
def aloqa():
    os.system('clear')
    for char in text10:
        print(Fore.BLUE + char, end='', flush=True)
        time.sleep(0.010)
        print(Style.RESET_ALL, end='')
    print()
    input_text = input(Fore.RESET + "\n    Dasturchi bilan bog'lanishni istaysizmi? y/n " + Fore.YELLOW + "❯❯" + Style.RESET_ALL)
    if input_text.lower() == 'y':
        link = 'https://t.me/Shoirjon_No1'
        webbrowser.open(link)
    main_menu()

def main_menu():
    print()
    for char in text0:
        print(Fore.RED + char, end='', flush=True)
        time.sleep(0.010)
        print(Style.RESET_ALL, end='')

    print()
    for char in text1:
        print(Fore.GREEN + char, end='', flush=True)
        time.sleep(0.010)
        print(Style.RESET_ALL, end='')

    print()
    for char in text2:
        print(Fore.BLUE + char, end='', flush=True)
        time.sleep(0.010)
        print(Style.RESET_ALL, end='')

    print()
    for char in text3:
        print(Fore.CYAN + char, end='', flush=True)
        time.sleep(0.010)
        print(Style.RESET_ALL, end='')

    print()
    for char in text4:
        print(Fore.CYAN + char, end='', flush=True)
        time.sleep(0.010)
        print(Style.RESET_ALL, end='')

    print()
    for char in text5:
        print(Fore.CYAN + char, end='', flush=True)
        time.sleep(0.010)
        print(Style.RESET_ALL, end='')

    print()
    for char in text6:
        print(Fore.CYAN + char, end='', flush=True)
        time.sleep(0.010)
        print(Style.RESET_ALL, end='')

    print()
    
    for char in text7:
        print(Fore.CYAN + char, end='', flush=True)
        time.sleep(0.010)
        print(Style.RESET_ALL, end='')

    print()
    
    for char in text8:
        print(Fore.CYAN + char, end='', flush=True)
        time.sleep(0.010)
        print(Style.RESET_ALL, end='')

    print()
    for char in text9:
        print(Fore.CYAN + char, end='', flush=True)
        time.sleep(0.010)
        print(Style.RESET_ALL, end='')

    a = int(input(Fore.RESET + "\n    TANLOVINGIZNI KIRITING " + Fore.YELLOW + "❯❯ " + Style.RESET_ALL))

    if a == 1:
        ornatish()
    elif a == 2:
        b()
    elif a == 3:
        c()
    elif a == 4:
        d()
    elif a == 5:
        ebout()
    elif a == 6:
        aloqa()
    elif a == 7:
        exit()

main_menu()
