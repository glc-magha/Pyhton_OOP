"""Inheritance (Türkçesi: Kalıtım), nesne yönelimli programlamada (OOP) bir sınıfın
(alt sınıf - subclass) başka bir sınıfın (üst sınıf - superclass) özelliklerini ve metotlarını miras almasıdır.

Bu sayede kod tekrarından kaçınılır ve daha modüler, sürdürülebilir yazılım geliştirilir.

Özellik	Açıklama
 Yeniden kullanım...	Üst sınıftaki kodlar alt sınıfa miras kalır.
 Kod tekrarı azaltılır...	Ortak işlevler tek bir yerde yazılır.
 Genişletilebilirlik	...Alt sınıf, üst sınıfın davranışını değiştirebilir (override).
 Hiyerarşik yapı	Gerçek dünyadaki "A bir B'dir" ilişkisi kodda temsil edilir.

# Üst sınıf (superclass)
class Hayvan:
    def hareket_et(self):
        print("Hayvan hareket ediyor")

# Alt sınıf (subclass)
class Kus(Hayvan):
    def uc(self):
        print("Kuş uçuyor")

# Kullanım
k = Kus()
k.hareket_et()  # Üst sınıftan miras
k.uc()          # Alt sınıfa ait

#çıktı
Hayvan hareket ediyor
Kuş uçuyor
#super() Fonksiyonu ile Üst Sınıfa Erişim
class Hayvan:
    def __init__(self, isim):
        self.isim = isim

    def tanit(self):
        print(f"Ben bir hayvanım: {self.isim}")

class Kopek(Hayvan):
    def __init__(self, isim, tur):
        super().__init__(isim)  # Üst sınıfın init'ini çağır
        self.tur = tur

    def tanit(self):  # Override ettik
        super().tanit()
        print(f"Türüm: {self.tur}")

        k = Kopek("Karabas", "Golden Retriever")
        k.tanit()
        #çıktı
Ben bir hayvanım: Karabas
Türüm: Golden Retriever


class Calisan:
    def calis(self):
        print("Çalışan çalışıyor.")

class Yazilimci(Calisan):
    def calis(self):
        print("Yazılım geliştiriyor.")

class Tasarimci(Calisan):
    def calis(self):
        print("Tasarım yapıyor.")

        personel = [Yazilimci(), Tasarimci()]

        for kisi in personel:
            kisi.calis()
"""