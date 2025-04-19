"""__init__ Nedir?
__init__ metodu, bir sınıftan yeni bir nesne oluşturulduğunda otomatik olarak çalışan özel bir metottur.

İngilizce “initialize” (başlatmak) kelimesinden gelir.

Sınıf içinde nesneye başlangıç verisi atamak için kullanılır

class Kisi:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
Açıklama:
self: Oluşturulan nesnenin kendisini temsil eder.

ad, yas: Nesne oluşturulurken dışarıdan alınan veriler.

self.ad = ad: Parametre olarak alınan ad, nesnenin ad özelliğine atanır.

class Ogrenci:
    def __init__(self, isim, numara):
        self.isim = isim
        self.numara = numara

    def tanit(self):
        print(f"Öğrenci: {self.isim}, Numara: {self.numara}")
o1 = Ogrenci("Ahmet", 123)
o2 = Ogrenci("Zeynep", 456)

o1.tanit()  # Öğrenci: Ahmet, Numara: 123
o2.tanit()  # Öğrenci: Zeynep, Numara: 456
__init__ Olmazsa Ne Olur?

class Araba:
    pass

a = Araba()  # Çalışır ama içi boştur.
__init__ metodu tanımlanmazsa, Python boş bir kurucu kullanır ama nesneye veri atanamaz.

#__init__ + inheritance

class Hayvan:
    def __init__(self, isim):
        self.isim = isim

class Kopek(Hayvan):
    def __init__(self, isim, tur):
        super().__init__(isim)   # Üst sınıfın init'ini çağır
        self.tur = tur

        #Kitap Sınıfı Örneği


        class Kitap:
            def __init__(self, ad, yazar, sayfa_sayisi):
                self.ad = ad
                self.yazar = yazar
                self.sayfa_sayisi = sayfa_sayisi

            def bilgi_goster(self):
                print(f"{self.ad} - {self.yazar} ({self.sayfa_sayisi} sayfa)")


        k1 = Kitap("Simyacı", "Paulo Coelho", 180)
        k1.bilgi_goster()



        #Kare Alan Hesabı Örneği
        class Kare:
            def __init__(self, kenar):
                self.kenar = kenar

            def alan(self):
                return self.kenar ** 2


        kare1 = Kare(5)
        print("Alan:", kare1.alan())

        #Kullanıcı Giriş  Sistemi(Basit)
    class Kullanici:
        def __init__(self, kullanici_adi, sifre):
            self.kullanici_adi = kullanici_adi
            self.sifre = sifre

        def giris_yap(self, girilen_sifre):
            if self.sifre == girilen_sifre:
                print("Giriş başarılı!")
            else:
                print("Hatalı şifre!")

    k1 = Kullanici("ayse123", "abc123")
    k1.giris_yap("abc123")  # Giriş başarılı!
    k1.giris_yap("yanlis")  # Hatalı şifre!"""