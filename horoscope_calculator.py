#Burc Hesaplama Sistemi 

def burc():
    ay = int(input("Doğum ayınızı giriniz (1-12): "))
    gün = int(input("Doğum gününüzü giriniz (1-31): "))

    # Geçersiz tarihleri kontrol etme

    if ay < 1 or ay > 12:
        print("Yanlış ay girdiniz! Lütfen tekrar deneyin.")
        burc()
        return
    elif gün < 1 or gün > 31:
        print("Yanlış gün girdiniz! Lütfen tekrar deneyin.")
        burc()
        return
    elif (ay == 2 and gün > 29) or (ay in [4, 6, 9, 11] and gün > 30):
        print("Bu ayda bu kadar gün yok! Lütfen tekrar deneyin.")
        burc()
        return

    # Burç hesaplama

    if (ay == 3 and gün >= 21) or (ay == 4 and gün <= 20):          #Koç Burcu - 21 Mart- 20 Nisan
        print("Koç burcusunuz.")
    elif (ay == 4 and gün >= 21) or (ay == 5 and gün <= 20):        #Boğa Burcu - 21 Nisan – 20 Mayıs
        print("Boğa burcusunuz.")
    elif (ay == 5 and gün >= 21) or (ay == 6 and gün <= 21):        #İkizler Burcu - 21 Mayıs – 21 Haziran
        print("İkizler burcusunuz.")
    elif (ay == 6 and gün >= 22) or (ay == 7 and gün <= 22):        #Yengeç Burcu - 22 Haziran – 22 Temmuz
        print("Yengeç burcusunuz.")
    elif (ay == 7 and gün >= 23) or (ay == 8 and gün <= 23):        #Aslan Burcu - 23 Temmuz – 23 Ağustos
        print("Aslan burcusunuz.")
    elif (ay == 8 and gün >= 24) or (ay == 9 and gün <= 23):        #Başak Burcu - 24 Ağustos – 23 Eylül
        print("Başak burcusunuz.")
    elif (ay == 9 and gün >= 24) or (ay == 10 and gün <= 23):       #Terazi Burcu - 24 Eylül – 23 Ekim
        print("Terazi burcusunuz.")
    elif (ay == 10 and gün >= 24) or (ay == 11 and gün <= 22):      #Akrep Burcu - 24 Ekim – 22 Kasım
        print("Akrep burcusunuz.")
    elif (ay == 11 and gün >= 23) or (ay == 12 and gün <= 21):      #Yay Burcu - 23 Kasım – 21 Aralık
        print("Yay burcusunuz.")
    elif (ay == 12 and gün >= 22) or (ay == 1 and gün <= 20):       #Oğlak Burcu - 22 Aralık – 20 Ocak
        print("Oğlak burcusunuz.")
    elif (ay == 1 and gün >= 21) or (ay == 2 and gün <= 19):        #Kova Burcu - 21 Ocak – 19 Şubat
        print("Kova burcusunuz.")
    elif (ay == 2 and gün >= 20) or (ay == 3 and gün <= 20):        #Balık Burcu - 20 Şubat – 20 Mart
        print("Balık burcusunuz.")

burc()