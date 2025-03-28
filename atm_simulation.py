# Banka ATM Simülasyonu

# Kullanıcı şifresi ve başlangıç bakiyesi belirleniyor
parola = "1234"  # Kullanıcı şifresi
bakiye = 100000  # Başlangıç bakiyesi

# Kullanıcıdan şifre girişi isteniyor
a = input("Hoşgeldiniz... Lütfen parolanızı giriniz:")
b = 0  # Yanlış giriş sayacı

# Şifre kontrolü döngüsü
while True:
    if a != parola:
        b += 1  # Yanlış giriş sayısını artır
        if b == 3:  # Üç başarısız girişten sonra çıkış
            print("Deneme hakkınız doldu. Çıkış yapılıyor...")
            exit()
        a = input("Parola yanlış. Lütfen tekrar deneyiniz:")
    else:
        break  # Doğru şifre girildiğinde döngüyü sonlandır

# Kullanıcı işlem menüsüne yönlendiriliyor
while True:

    print("\n---İŞLEMLER---")
    print("[1] Bakiye Sorgula")
    print("[2] Para Yatır")
    print("[3] Para Çek")
    print("[a] Şifre Değiştir")
    print("[q] Çıkış")
    islem = input("Yapmak istediğiniz işlemi seçiniz: ")

    # Şifre değiştirme işlemi
    if islem.lower() == "a":
        while True:
            yeni_sifre = input("Yeni şifrenizi giriniz: ")
            if yeni_sifre.lower() == parola.lower():
                print("Yeni şifreniz eski şifrenizle aynı olamaz. Lütfen farklı bir şifre giriniz.")
                continue
            yeni_sifre_tekrar = input("Yeni şifrenizi tekrar giriniz: ")
            if yeni_sifre != yeni_sifre_tekrar:
                print("Şifreler uyuşmuyor. Lütfen tekrar deneyiniz.")
                continue
            parola = yeni_sifre  # Şifre güncelleniyor
            print("Şifreniz başarıyla değiştirildi.")
            break

    # Bakiye sorgulama
    elif islem == "1":
        print("Güncel bakiyeniz:", bakiye)

    # Para çekme işlemi
    elif islem == "2":
        while True:
            try:
                cit = int(input("Çekmek istediğiniz tutarı giriniz: "))
                if cit > bakiye:
                    print("Yetersiz bakiye. Mevcut bakiyeniz:", bakiye)
                elif cit <= 0:
                    print("Geçersiz tutar. Lütfen pozitif bir değer giriniz.")
                else:
                    bakiye -= cit  # Bakiyeden çekilen miktarı düş
                    print("İşleminiz başarılı. Güncel bakiyeniz:", bakiye)
                    break
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz.")  # Hatalı giriş kontrolü

    # Para yatırma işlemi
    elif islem == "3":
        while True:
            try:
                yit = int(input("Yatırmak istediğiniz tutarı giriniz: "))
                if yit <= 0:
                    print("Geçersiz tutar. Lütfen pozitif bir değer giriniz.")
                else:
                    bakiye += yit  # Bakiyeye yatırılan miktarı ekle
                    print("İşleminiz başarılı. Güncel bakiyeniz:", bakiye)
                    break
            except ValueError:
                print("Lütfen geçerli bir sayı giriniz.")  # Hatalı giriş kontrolü

    # Çıkış yapma işlemi
    elif islem.lower() == "q":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Hatalı giriş! Lütfen geçerli bir işlem giriniz.")
        