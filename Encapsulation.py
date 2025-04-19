"""Encapsulation (Kapsülleme) Nedir?
Encapsulation, nesne yönelimli programlamada (OOP) verileri ve metotları dış müdahalelere karşı korumak,
yani kontrollü erişim sağlamak için kullanılır.

 Amaç:
Veri gizliliğini sağlamak (örneğin şifre gibi hassas verileri korumak)
Kodun sadece belirli bölümlerine dışarıdan erişime izin vermek
Hataları azaltmak ve güvenliği artırmak

Python’da Encapsulation Nasıl Yapılır?
Python'da:


#Erişim Tipi	Sembol	Açıklama
Public (her yerden erişilir)
self.veri
Genel kullanım, dışarıdan erişilebilir


Protected (yarı gizli)
self._veri
Uyarı niteliğinde, erişilmemeli

Private (tam gizli)
self.__veri
Dışarıdan erişilemez (name mangling)

class BankaHesabi:
    def __init__(self, isim, bakiye):
        self.isim = isim
        self.__bakiye = bakiye  # private değişken

    def bakiye_goster(self):
        print(f"{self.isim} adlı kullanıcının bakiyesi: {self.__bakiye} TL")

    def para_cek(self, miktar):
        if miktar <= self.__bakiye:
            self.__bakiye -= miktar
            print(f"{miktar} TL çekildi.")
        else:
            print("Yetersiz bakiye!")

#Dışarıdan erişmeye çalışırsan:
print(hesap.__bakiye)
 Hata verir çünkü __bakiye değişkeni gizlenmiştir (private).

Getter & Setter Metotları

class Ogrenci:
    def __init__(self, isim):
        self.__isim = isim

    def get_isim(self):
        return self.__isim

    def set_isim(self, yeni_isim):
        if isinstance(yeni_isim, str) and len(yeni_isim) > 2:
            self.__isim = yeni_isim
        else:
            print("Geçersiz isim!")

o = Ogrenci("Ayşe")
print(o.get_isim())  # Ayşe
o.set_isim("Mehmet")
print(o.get_isim())  # Mehmet


Encapsulation
Veriyi gizlemek ve sadece kontrollü erişim sağlamak

__ (double underscore)
Değişkeni gizler (private yapar)

Getter/Setter
Veri okumak ve güncellemek için güvenli metotlar

#Basit Şifreli Kullanıcı Sistemi

class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.__sifre = sifre  # şifre gizli (private)

    def giris_yap(self, girilen_sifre):
        if girilen_sifre == self.__sifre:
            print(f"Giriş başarılı. Hoş geldin, {self.kullanici_adi}!")
        else:
            print("Hatalı şifre!")

    def sifre_degistir(self, eski_sifre, yeni_sifre):
        if eski_sifre == self.__sifre:
            self.__sifre = yeni_sifre
            print("Şifre başarıyla değiştirildi.")
        else:
            print("Eski şifre yanlış. Değiştirilemedi.")

    def get_sifre(self):
        return "Bu bilgiye erişim izniniz yok 😎"
 Kullanım

k1 = Kullanici("ayse123", "gizli123")

# Şifreyi görmeye çalış
print(k1.get_sifre())  # gizli şifreye doğrudan erişim yok

# Giriş yapmayı dene
k1.giris_yap("yanlis")     # Hatalı şifre!
k1.giris_yap("gizli123")   # Giriş başarılı

# Şifre değiştirmeyi dene
k1.sifre_degistir("hatalı", "yeni123")  # Eski şifre yanlış
k1.sifre_degistir("gizli123", "yeni123")  # Başarılı

# Yeni şifreyle tekrar giriş
k1.giris_yap("yeni123")  # Giriş başarılı

Neden Encapsulation?

__sifre	Dışarıdan erişilemez → koruma sağlar
sifre_degistir()	Şifreyi kontrol ederek değiştirme
giris_yap()	Doğrulama sağlar
get_sifre()	Bilgiyi gizler, şifreyi göstermez

 #Şifre güvenliği açısından şifreleri düz metin olarak saklamak çok risklidir. Bu yüzden genellikle hashing (karma) yöntemi kullanılır.

Python’da şifreleri güvenli şekilde saklamak için en çok kullanılan modüllerden biri: hashlib

 Şifre Karma (Hash) Nedir?
Şifre düz metin olarak değil, tek yönlü bir algoritma ile şifrelenerek saklanır.

En yaygın algoritmalar: SHA-256, SHA-1, MD5 (ama MD5 artık önerilmez).

Geri çözülemez → sadece doğrulama için kullanılır.

 Örnek: Kullanıcı Sınıfı + Hashli Şifre

import hashlib

class Kullanici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.__sifre_hash = self.__sifre_hashle(sifre)

    def __sifre_hashle(self, sifre):
        return hashlib.sha256(sifre.encode()).hexdigest()

    def giris_yap(self, girilen_sifre):
        if self.__sifre_hash == self.__sifre_hashle(girilen_sifre):
            print(f"Giriş başarılı. Hoş geldin, {self.kullanici_adi}!")
        else:
            print("Hatalı şifre!")

    def sifre_degistir(self, eski_sifre, yeni_sifre):
        if self.__sifre_hash == self.__sifre_hashle(eski_sifre):
            self.__sifre_hash = self.__sifre_hashle(yeni_sifre)
            print("Şifre başarıyla değiştirildi.")
        else:
            print("Eski şifre yanlış. Değiştirilemedi.")

    def sifreyi_goster(self):
        return self.__sifre_hash  # sadece hash'i gösterir
 Kullanım:

k1 = Kullanici("mehmet", "12345")

print("Kayıtlı şifre (hash):", k1.sifreyi_goster())

k1.giris_yap("12345")     # Giriş başarılı
k1.giris_yap("yanlis")    # Hatalı şifre!

k1.sifre_degistir("12345", "abc123")
k1.giris_yap("abc123")    # Giriş başarılı
 Hash'li Şifre Örneği:

hashlib.sha256("12345".encode()).hexdigest()
 Çıktı (örnek):

#çıktı örneği
5994471abb01112afcc18159f6cc74b4f511b99806da5ec8a4c1d1e7c4d8f7f0
"""