# Basit sayı tahmin oyunu 
      
import random  # random modülü rastgele sayı üretir

# 1 ile 100 arasında rastgele bir sayı tuttu
sayi = random.randint(1, 100)

# 5 tahmin hakkı 
tahmin_hakki = 5

print("Basit Sayı Tahmin Oyununa Hoşgeldiniz!")

# Tahmin hakkı bitene kadar döngü devam eder
while tahmin_hakki > 0:
    try:
        # Kullanıcıdan tahmin girmesi isteniyor
        tahmin = int(input("Sayıyı tahmin ediniz: "))
    except ValueError:
        # Kullanıcı geçersiz karakter girerse hata mesajı verilir
        print("Lütfen sadece bir sayı giriniz.")
        continue  # Döngüyü başa sarılır, tekrar giriş yaptırılır

    # Tahmin doğruysa oyun bitiyor

    if tahmin == sayi:
        print("Doğru tahmin! Tebrikler")
        break
    # Kullanıcının tahmini rastgele sayıdan büyük
    elif tahmin > sayi:
        print("Yanlış tahmin! Daha küçük bir sayı giriniz.")
    # Kullanıcının tahmini rastgele sayıdan küçük
    else:
        print("Yanlış tahmin! Daha büyük bir sayı giriniz.")

    # Her yanlış tahminde tahmin hakkını bir azaltır
    tahmin_hakki -= 1
    print(f"Kalan tahmin hakkınız: {tahmin_hakki}")

    # Kullanıcının tahmin hakkı bittiğinde oyun biter
    if tahmin_hakki == 0:
        print(f"Tahmin hakkınız doldu! Doğru cevap: {sayi}")

print("Oyun bitti. Tekrar oynamak için programı yeniden çalıştırın.")        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        