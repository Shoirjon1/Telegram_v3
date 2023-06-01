import csv

# Telefon raqamlarini o'qish
def read_phone_numbers():
    with open('phone.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        numbers = [row[0] for row in reader]
    return numbers

# Telefon raqamlarini o'chirish
def delete_number(index):
    numbers = read_phone_numbers()
    if index < 1 or index > len(numbers):
        print("Noto'g'ri raqam indeksi! Iltimos, qayta kiriting.")
        return
    deleted_number = numbers.pop(index - 1)
    with open('phone.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for number in numbers:
            writer.writerow([number])
    print(f"{deleted_number} raqami o'chirildi.")

# Telefon raqamlarini ko'rish, o'chirish uchun menyu
def main_menu():
    while True:
        print("\nTelefon raqamlari menu:")
        print("1. Telefon raqamlarini ko'rish")
        print("2. Raqam qo'shish")
        print("3. Raqam o'chirish")
        print("4. Chiqish")
        choice = input("Tanlang (1/2/3/4): ")
        if choice == '1':
            print("\nTelefon raqamlari:")
            numbers = read_phone_numbers()
            for index, number in enumerate(numbers, start=1):
                print(f"{index}. {number}")
        elif choice == '2':
             print("\nTelefon raqamlari:")
             
             numbers = read_phone_numbers()
             
             for index, number in enumerate(numbers, start=1):
                
                print(f"{index}. {number}")
                print("\nTelefon raqamlarini kiriting:")
                new_numbers = input("Qo'shish uchun raqamlarni kiritgan holda vergul bilan ajratib yozing: ")
                new_numbers = new_numbers.split(',')
                with open('phone.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    for number in new_numbers:
                        writer.writerow([number.strip()])
        elif choice == '3':
            print("\nTelefon raqamlari:")
            numbers = read_phone_numbers()
            for index, number in enumerate(numbers, start=1):
                print(f"{index}. {number}")
            index = int(input("O'chirish uchun raqam indeksini kiriting: "))
            delete_number(index)
        elif choice == '4':
            break
        else:
            print("Noto'g'ri tanlov! Iltimos, qayta kiriting.")

# Boshlang'ich menyuni ishga tushirish
main_menu()
