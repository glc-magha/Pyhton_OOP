"""#Abstraction (Soyutlama) Nedir?
Abstraction, karmaşık sistemleri sadeleştirerek sadece gerekli olan detayları ortaya çıkarmak ve gereksiz detayları gizlemek anlamına gelir.

 Kısaca:
“Ne yaptığını göster, nasıl yaptığını sakla.”

 Gerçek Hayattan Örnek
Bir arabanın gaz pedalına bastığında arabanın hızlandığını bilirsin ama:
Motorun nasıl çalıştığını
Ateşlemenin nasıl olduğunu
Yağın nasıl pompalandığını
bilmen gerekmez. İşte bu bir soyutlamadır!

# Yazılımda Abstraction
Yazılımda abstraction, genellikle:

Arayüz (interface) veya
Soyut sınıflar (abstract class)
ile yapılır.

Ama Python’da arayüz kavramı yoktur. Onun yerine soyut sınıflar (ABC modülü ile) kullanılır.
 Python’da Abstraction Nasıl Yapılır?

from abc import ABC, abstractmethod

class Hayvan(ABC):  # soyut sınıf
    @abstractmethod
    def ses_cikar(self):
        pass
Yukarıdaki örnekte:

Hayvan bir soyut sınıftır.

#ses_cikar() fonksiyonu sadece tanımlanmış ama içi yazılmamış → "ne yapılacak?" belli, "nasıl?" kısmı alt sınıflara bırakılmıştır.

 Alt Sınıflar – Soyut Sınıfı Uygulayanlar

class Kedi(Hayvan):
    def ses_cikar(self):
        print("Miyav!")

class Kopek(Hayvan):
    def ses_cikar(self):
        print("Hav hav!")
# Kullanım:

kedi1 = Kedi()
kopek1 = Kopek()

kedi1.ses_cikar()   # Miyav!
kopek1.ses_cikar()  # Hav hav!
 #Direkt Soyut Sınıfla Nesne Oluşturulamaz:

h = Hayvan()  #  Hata verir
Çünkü Hayvan soyut bir sınıftır ve eksik tanımlıdır.

# Neden Abstraction Kullanılır?

Avantaj	Açıklama
 Basitleştirme	Kullanıcıya sadece ne yapacağını gösterir
 Güvenlik	Gereksiz detayları gizler
Yeniden kullanılabilirlik	Alt sınıflar istedikleri gibi uygular
 Genişletilebilirlik	Yeni türler kolayca eklenebilir
 Fark: Abstraction vs Encapsulation

Terim	Amaç
Encapsulation	Veriyi gizlemek (nasıl erişileceğini kontrol etmek)
Abstraction	Detayları gizleyip, önemli olanı göstermek


#Bu örnekte soyutlama ile her hayvanın ortak yönlerini soyutlayacak, ama detaylı davranışları her türe göre ayrı ayrı tanımlayacağız.

 Plan:
Soyut sınıf: Hayvan

ses_cikar(), bilgi_ver() gibi metotlar tanımlanacak ama içi yazılmayacak.

Alt sınıflar: Aslan, Fil, Timsah, Kaplumbaga vs.

Bu sınıflar kendi türlerine özgü davranışları uygulayacak.

Kullanıcı: Hayvanları çağıracak, seslerini duyacak, bilgi alacak.

🐾 Kod:

from abc import ABC, abstractmethod

# Soyut Sınıf
class Hayvan(ABC):
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    @abstractmethod
    def ses_cikar(self):
        pass

    @abstractmethod
    def bilgi_ver(self):
        pass
 Alt Sınıflar

class Aslan(Hayvan):
    def ses_cikar(self):
        print("ROAAARRR!")

    def bilgi_ver(self):
        print(f"{self.isim} adlı aslan {self.yas} yaşında ve etoburdur.")

class Fil(Hayvan):
    def ses_cikar(self):
        print("Trrrrrr! 🐘")

    def bilgi_ver(self):
        print(f"{self.isim} adlı fil {self.yas} yaşında ve otoburdur.")

class Timsah(Hayvan):
    def ses_cikar(self):
        print("Grrrrrr! ")

    def bilgi_ver(self):
        print(f"{self.isim} adlı timsah {self.yas} yaşında ve yarı sucul bir canlıdır.")

class Kaplumbaga(Hayvan):
    def ses_cikar(self):
        print("...")  # Sessiz olabilir :)

    def bilgi_ver(self):
        print(f"{self.isim} adlı kaplumbağa {self.yas} yaşında ve çok sabırlıdır.")
# Kullanım

hayvanlar = [
    Aslan("Simba", 5),
    Fil("Dumbo", 12),
    Timsah("Kroko", 7),
    Kaplumbaga("Tosbik", 80)
]

for hayvan in hayvanlar:
    hayvan.bilgi_ver()
    hayvan.ses_cikar()
    print("---")
 Çıktı:

Simba adlı aslan 5 yaşında ve etoburdur.
ROAAARRR!
---
Dumbo adlı fil 12 yaşında ve otoburdur.
Trrrrrr! 🐘
---
Kroko adlı timsah 7 yaşında ve yarı sucul bir canlıdır.
Grrrrrr! 🐊
---
Tosbik adlı kaplumbağa 80 yaşında ve çok sabırlıdır.
...



"""