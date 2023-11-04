import random
import time

print("""Sayı tahmin oyunu
1 ile 40 arasında sayıyı tahmin edin
""")

rastgele_sayi=random.randint(1,40)
tahmin_hakki=7
while True:
    tahmin=int(input("Tahmin edeniz: "))
    if tahmin==rastgele_sayi:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler bildiniz")
        break
    else:
        if rastgele_sayi>tahmin:
            print("Bilgiler sorgulanıyor...")
            time.sleep(0.5)
            print("Bilemediniz yukarı çıkınız")
            tahmin_hakki -= 1
        else:
            print("Bilgiler sorgulanıyor...")
            time.sleep(0.5)
            print("Bilemediniz aşağı ininiz")
            tahmin_hakki -= 1
        if tahmin_hakki==0:
            print("Kaybettiniz")
            break
