print("SILANURUN DONDURMA DÜKKANINA HOŞGELDİNİZZZZ")

"""
DONDURMA TÜRLERİ:
Çilekli için 1'i     (TOPU 25 TL)
Kakaolu için 2'yi    (TOPU 30 TL)
Limonlu için 3'ü     (TOPU 50 TL)
Vanilyalı için 4'ü   (TOPU 20 TL)
Kavunlu için 5'i     (TOPU 45 TL)
tuşlayınız...

"""

x = int(input("Kaç top dondurma istersiniz? "))
kulah = list()

for i in range(x):
    while True:
        a = int(input("Bu topunuz hangi çeşit olsun? "))
        
        if  1 <= a <=5:
            kulah.append(a)
            break
        else:
            print("Yanlış değer girdiniz tekrar deneyin")
            
            
                       
print( kulah.count(1),"top çilekli\n" ,kulah.count(2), "top kakaolu\n",kulah.count(3), "top limonlu\n",kulah.count(5), "top kavunlu\n", kulah.count(4), "top vanilyalı dondurmanız HAZIIIRRR.....")   

fiyat = 25 * kulah.count(1) + kulah.count(2) * 30 + 50 * kulah.count(3) + kulah.count(4) * 20 + kulah.count(5) * 45

print("Ödemeniz gereken ücret" , fiyat , "tır.")     
            
            
    
        
        
        
