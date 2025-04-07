class Araba:
    renk = "kırmızı"  # özellik
    def calistir(self):  # davranış
        print("Araba çalıştı.")

#object
araba1 = Araba()
print(araba1.renk)         # kırmızı
araba1.calistir()          # Araba çalıştı.


#Constructor (Kurucu Metot): __init__()
#Her nesne oluşurken ilk çalışan fonksiyondur. Genellikle özellikleri tanımlamak için kullanılır.
class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgileri_goster(self):
        print(f"{self.marka} - {self.model}")

araba2 = Araba("Toyota", "Corolla")
araba2.bilgileri_goster()  # Toyota - Corolla


#Kapsülleme (Encapsulation)
#erileri gizlemek ve sadece belirli yollarla erişilmesini sağlamak
class Kisi:
    def __init__(self, isim, yas):
        self.isim = isim
        self.__yas = yas  # __ ile gizli hale gelir

    def yas_goster(self):
        print(self.__yas)

k = Kisi("Ahmet", 25)
k.yas_goster()     # 25
# print(k.__yas)   # Hata verir!


#Kalıtım (Inheritance)
#Bir sınıfın başka bir sınıftan özellik ve metotları miras almasıdır.
class Hayvan:
    def ses_cikar(self):
        print("Ses çıkarır")

class Kedi(Hayvan):  # Hayvan sınıfından kalıtım alıyor
    def miyavla(self):
        print("Miyav!")

kedi = Kedi()
kedi.ses_cikar()  # Ses çıkarır
kedi.miyavla()    # Miyav!

#Çok Biçimlilik (Polymorphism)
# Aynı isimli metodun farklı sınıflarda farklı şekilde çalışmasıdır.
class Kopek:
    def ses_cikar(self):
        print("Hav hav!")

class Kedi:
    def ses_cikar(self):
        print("Miyav!")

def ses_ver(hayvan):
    hayvan.ses_cikar()

ses_ver(Kopek())  # Hav hav!
ses_ver(Kedi())   # Miyav!


# Öğrenci Kayıt Sistemi (OOP)
#Öğrenci sınıfı: İsim, soyisim, numara, sınıf bilgisi
#

class Ogrenci:
    def __init__(self, isim, soyisim, numara, sinif):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.sinif = sinif

    def bilgileri_goster(self):
        print(f"{self.numara} - {self.isim} {self.soyisim} | Sınıf: {self.sinif}")


class OgrenciKayitSistemi:
    def __init__(self):
        self.ogrenciler = []

    def ogrenci_ekle(self, ogrenci):
        self.ogrenciler.append(ogrenci)
        print(f"{ogrenci.isim} {ogrenci.soyisim} başarıyla eklendi.")

    def ogrencileri_listele(self):
        if not self.ogrenciler:
            print("Kayıtlı öğrenci yok.")
            return
        for ogr in self.ogrenciler:
            ogr.bilgileri_goster()

    def ogrenci_sil(self, numara):
        for ogr in self.ogrenciler:
            if ogr.numara == numara:
                self.ogrenciler.remove(ogr)
                print(f"{numara} numaralı öğrenci silindi.")
                return
        print("Öğrenci bulunamadı.")


# 🧪 Kullanım
sistem = OgrenciKayitSistemi()

ogr1 = Ogrenci("Ali", "Yılmaz", "1001", "10A")
ogr2 = Ogrenci("Ayşe", "Demir", "1002", "11B")

sistem.ogrenci_ekle(ogr1)
sistem.ogrenci_ekle(ogr2)

print("\n🔍 Kayıtlı Öğrenciler:")
sistem.ogrencileri_listele()

print("\n🗑️ Öğrenci Silme:")
sistem.ogrenci_sil("1001")

print("\n📋 Güncel Liste:")
sistem.ogrencileri_listele()

#Banka Hesabı Sistemi (OOP)
#Hesap oluşturma (isim, bakiye, hesap numarası)
#Bakiye görüntüleme
#Para yatırma
#Para çekme (bakiye kontrolü ile)
#Hesap bilgisi gösterme

class BankaHesabi:
    def __init__(self, isim, hesap_no, bakiye=0):
        self.isim = isim
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def hesap_bilgileri(self):
        print(f"Hesap Sahibi: {self.isim}")
        print(f"Hesap No     : {self.hesap_no}")
        print(f"Bakiye       : {self.bakiye} TL")

    def bakiye_goster(self):
        print(f"{self.isim} adlı kullanıcının bakiyesi: {self.bakiye} TL")

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz miktar!")

    def para_cek(self, miktar):
        if miktar > 0 and miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL")
        else:
            print("Yetersiz bakiye veya geçersiz miktar!")


hesap1 = BankaHesabi("Mehmet Yılmaz", "TR100200300", 5000)

print("🏦 Hesap Bilgileri:")
hesap1.hesap_bilgileri()

print("\n💸 Para Yatırma:")
hesap1.para_yatir(1500)

print("\n💳 Para Çekme:")
hesap1.para_cek(2000)

print("\n📊 Güncel Bakiye:")
hesap1.bakiye_goster()
#Hesap Sınıfı:
import datetime

class BankaHesabi:
    def __init__(self, isim, hesap_no, sifre, bakiye=0):
        self.isim = isim
        self.hesap_no = hesap_no
        self.__sifre = sifre
        self.bakiye = bakiye
        self.gecmis = []

    def giris_yap(self, sifre):
        return self.__sifre == sifre

    def hesap_bilgileri(self):
        print(f"Hesap Sahibi : {self.isim}")
        print(f"Hesap No     : {self.hesap_no}")
        print(f"Bakiye       : {self.bakiye} TL")

    def bakiye_goster(self):
        print(f"Bakiye: {self.bakiye} TL")

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            self.__log_ekle(f"{miktar} TL yatırıldı.")
            print(f"{miktar} TL başarıyla yatırıldı.")
        else:
            print("Geçersiz miktar.")

    def para_cek(self, miktar):
        if miktar > 0 and miktar <= self.bakiye:
            self.bakiye -= miktar
            self.__log_ekle(f"{miktar} TL çekildi.")
            print(f"{miktar} TL başarıyla çekildi.")
        else:
            print("Yetersiz bakiye veya geçersiz miktar.")

    def islem_gecmisi(self):
        if not self.gecmis:
            print("Hiç işlem yapılmamış.")
        else:
            print("\n📜 İşlem Geçmişi:")
            for log in self.gecmis:
                print(log)

    def __log_ekle(self, mesaj):
        zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.gecmis.append(f"[{zaman}] {mesaj}")
#Hesap Yönetimi:
class BankaSistemi:
    def __init__(self):
        self.hesaplar = {}

    def hesap_ekle(self, hesap):
        self.hesaplar[hesap.hesap_no] = hesap

    def giris(self, hesap_no, sifre):
        hesap = self.hesaplar.get(hesap_no)
        if hesap and hesap.giris_yap(sifre):
            print(f"Giriş başarılı! Hoş geldiniz {hesap.isim}!")
            return hesap
        else:
            print("Hatalı hesap numarası veya şifre.")
            return None
#Kullanım:
# Banka sistemi oluştur
sistem = BankaSistemi()

# Örnek hesaplar oluştur
hesap1 = BankaHesabi("Ali Veli", "TR123", "1234", 10000)
hesap2 = BankaHesabi("Ayşe Kaya", "TR456", "4567", 7000)

# Sisteme hesapları ekle
sistem.hesap_ekle(hesap1)
sistem.hesap_ekle(hesap2)

# Giriş yap
no = input("Hesap No: ")
sifre = input("Şifre: ")

aktif_hesap = sistem.giris(no, sifre)

if aktif_hesap:
    while True:
        print("\n1- Bakiye Görüntüle\n2- Para Yatır\n3- Para Çek\n4- İşlem Geçmişi\n5- Çıkış")
        secim = input("Seçiminiz: ")

        if secim == "1":
            aktif_hesap.bakiye_goster()
        elif secim == "2":
            miktar = float(input("Yatırılacak miktar: "))
            aktif_hesap.para_yatir(miktar)
        elif secim == "3":
            miktar = float(input("Çekilecek miktar: "))
            aktif_hesap.para_cek(miktar)
        elif secim == "4":
            aktif_hesap.islem_gecmisi()
        elif secim == "5":
            print("Çıkış yapıldı.")
            break
        else:
            print("Geçersiz seçim!")
