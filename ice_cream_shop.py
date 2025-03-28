#İce Cream Shop
           
print("DONDURMA DÜKKANINA HOŞGELDİNİZZZZ")

"""
DONDURMA TÜRLERİ:
Çilekli için 1'i     (TOPU 25 TL)
Kakaolu için 2'yi    (TOPU 30 TL)
Limonlu için 3'ü     (TOPU 50 TL)
Vanilyalı için 4'ü   (TOPU 20 TL)
Kavunlu için 5'i     (TOPU 45 TL)
tuşlayınız...

"""

# Dondurma fiyatlarını içeren sözlük
fiyatlar = {1: 25, 2: 30, 3: 50, 4: 20, 5: 45}

# Kullanıcıdan kaç top istediğini al
while True:
    try:
        x = int(input("Kaç top dondurma istersiniz? "))
        if x <= 0:
            print("Lütfen pozitif bir sayı girin.")
        else:
            break
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

kulah = []

# Kullanıcıdan her top için dondurma çeşidini sorma
for i in range(x):
    while True:
        try:
            a = int(input(f"{i+1}. topunuz hangi çeşit olsun? (1-5): "))
            if 1 <= a <= 5:
                kulah.append(a)
                break
            else:
                print("Yanlış değer girdiniz, lütfen 1-5 arasında bir değer girin.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

# Her çeşit dondurmanın sayısını hesaplama
adetler = {i: kulah.count(i) for i in fiyatlar.keys()}

# Sipariş Özeti
print("\nSİPARİŞİNİZ:")
for key, value in adetler.items():
    if value > 0:
        print(f"- {value} top {['Çilekli', 'Kakaolu', 'Limonlu', 'Vanilyalı', 'Kavunlu'][key-1]}")

# Toplam fiyat hesaplama
toplam_fiyat = sum(adetler[key] * fiyatlar[key] for key in fiyatlar)

print(f"\nÖdemeniz gereken toplam ücret: {toplam_fiyat} TL\n")
print("Afiyet olsun! ")
