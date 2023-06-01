import random
import time

def print_with_random_colors(text):
    for line in text.split('\n'):
        for char in line:
            color_code = random.randint(30, 37)  # Tasodifiy rang kodi tanlash
            print(f"\033[1;{color_code}m{char}\033[0m", end='', flush=True)
            time.sleep(0.010)
        print()  # Qatorni boshatish
    print()

# Fayl nomini kiritish
filename = "info.txt"

# Faylni o'qish
with open(filename, "r") as file:
    text = file.read()

# Matnni har bir harf uchun tasodifiy bir rang bilan chiqarish
print_with_random_colors(text)
