import time

print("Hello, it PasswordChek")
english = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
spanish = "ñáéíóúüÑÁÉÍÓÚÜ"
french = "àâæçéèêëîïôœùûüÿÀÂÆÇÉÈÊËÎÏÔŒÙÛÜŸ"
special = "+_=*&!@#$%^()-/||"
while True:
    
    count = 0
    password = input("Введите ваш пароль: ")
    if len(password) < 8:
        count = count
    else:
        count += 1

    coun = sum(1 for i in password if i.isupper())
    if coun >= 3:
        count +=1

    else:
        count = count+1

    num_count = sum(1 for i in password if i.isdigit())
    if num_count >= 1:
        count += 1 
    if num_count >= 3:
        count += 1


    special_count = sum(1 for j in password if j in special)
    if special_count >= 1:
            count += 1 
    if special_count >= 3:
        count += 1


    low_password = password.lower()


    eng = sum(1 for j in password if j in english)
    rus = sum(1 for j in password if j in russian)
    span = sum(1 for j in password if j in spanish)
    fren = sum(1 for j in password if j in french)

    pul1 = sum(1 for j in password if j in english or j in russian or j in spanish or j in french)
    if pul1 >= 3:
        count +=1
    else:
        count = count

    if eng > 0 and rus > 0:
        count+=6
    else:
        count = count

    if eng > 0 and span > 0:
            count+=6
    else:
        count = count

    if eng > 0 and fren > 0:
                count+=6
    else:
        count = count

    print("Ваш балл от 0 до 23:", count)

    if count <= 5:
        print("Уровень безопасности: НИЗКИЙ 🔴")
    elif 6 <= count <= 10:
        print("Уровень безопасности: СРЕДНИЙ 🟡")
    else:
        print("Уровень безопасности: ВЫСОКИЙ 🟢")

    choi = input("Введите W если хотите выйти: ").lower()
    if choi == "y":
        print("Пока!")
        break
    else:
        continue

