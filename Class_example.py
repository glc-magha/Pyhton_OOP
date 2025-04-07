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