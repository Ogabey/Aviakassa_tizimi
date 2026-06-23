from db import get_connection

from Avia_CRUD import (
    parvoz_qoshish,
    barcha_parvozlar,
    parvoz_yangilash,
    parvoz_ochirish,
    shahar_boyicha_qidirish,
    chipta_band_qilish
)

while True:
    print("\n1. Parvoz qo'shish")
    print("2. Barcha parvozlar")
    print("3. Narx yangilash")
    print("4. Parvoz o'chirish")
    print("5. Shahar qidirish")
    print("6. Chipta band qilish")
    print("0. Chiqish")


    tanlov = input("Tanlang: ")


    if tanlov == "1":
        fn = input("Parvoz raqami: ")
        dep = input("Jo'nash aeroporti ID: ")
        arr = input("Kelish aeroporti ID: ")
        vaqt = input("Vaqt: ")
        narx = input("Narx: ")
        joy = input("Bo'sh joylar: ")
        parvoz_qoshish(fn, dep, arr, vaqt, narx, joy)


    elif tanlov == "2":
        barcha_parvozlar()


    elif tanlov == "3":
        fid = input("Parvoz ID: ")
        narx = input("Yangi narx: ")
        parvoz_yangilash(fid, narx)


    elif tanlov == "4":
        fid = input("Parvoz ID: ")
        parvoz_ochirish(fid)


    elif tanlov == "5":
        shahar = input("Shahar: ")
        shahar_boyicha_qidirish(shahar)


    elif tanlov == "6":
        fid = input("Parvoz ID: ")
        pid = input("Yo'lovchi ID: ")
        joy = input("Nechta joy: ")
        chipta_band_qilish(fid, pid, joy)


    elif tanlov == "0":
        print("Siz tizimdan chiqdingiz, etiboringiz uchun rahmat")
        break

    
    else:
        print("siz nomalum buyruq turini tanladingiz:(")