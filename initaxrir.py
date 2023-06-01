import configparser
import time

# .ini faylini o'qish
config = configparser.ConfigParser()
config.read('config.ini')

# Qiymatlarni o'qish
from_group = config.get('Shoirjon_official', 'fromgroup')
to_group = config.get('Shoirjon_official', 'ToGroup')
group_id = config.get('Shoirjon_official', 'GroupID')
phone_number = config.get('Shoirjon_official', 'PhoneNumber')

# Yangi qiymatlarni olish
new_from_group = input("Qaysi guruhdan obunachi olishni istaysiz? : ")
new_to_group = input("Qaysi guruhga obunachi qo'shishni istaysiz? : ")
new_group_id = input("Qo'shishni istagan guruhingiz ID raqamini kiriting: ")
new_phone_number = input("Obunachilarni to'plashim uchun raqam kiriting: ")

# Yangi qiymatlarni o'zgartirish
config.set('Shoirjon_official', 'fromgroup', new_from_group)
config.set('Shoirjon_official', 'ToGroup', new_to_group)
config.set('Shoirjon_official', 'GroupID', new_group_id)
config.set('Shoirjon_official', 'PhoneNumber', new_phone_number)

# .ini fayliga o'zgarishlarni saqlash
with open('config.ini', 'w') as configfile:
    config.write(configfile)

print("Barchasini eslab qoldim!\n    Davom etamiz!")
time.sleep(3)
