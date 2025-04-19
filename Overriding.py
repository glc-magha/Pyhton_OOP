"""Overriding (Türkçesiyle "geçersiz kılma" ya da "üstüne yazma"), nesne yönelimli programlama
(OOP)'da bir alt sınıfın (subclass), üst sınıfından (superclass) miras aldığı bir metodu kendi ihtiyacına göre yeniden tanımlaması anlamına gelir.

Overriding Nedir?
Amaç: Kalıtım (inheritance) yoluyla gelen bir metodu alt sınıfta farklı bir davranışla yeniden yazmak.

Kullanım: Genellikle çok biçimlilik (polymorphism) ile birlikte kullanılır.

Dil: Java, C#, Python, Apex (Salesforce), C++ gibi dillerde vardır.

class Hayvan {
    void sesCikar() {
        System.out.println("Hayvan ses çıkarıyor");
    }
}

class Kedi extends Hayvan {
    @Override
    void sesCikar() {
        System.out.println("Miyav!");
    }
}

#java
Hayvan
h = new
Kedi();
h.sesCikar(); // Çıktı: Miyav!

Overriding Özellikleri:

Özellik	Açıklama
📦 Kalıtım	Override işlemi için kalıtım olması gerekir.
🔄 Aynı İsim	Metod adı ve parametreler aynı olmalıdır.
⚠️ Erişim	Alt sınıf metodu, üst sınıf metodundan daha dar bir erişime sahip olamaz.
📢 @Override	Java gibi dillerde override yapıldığını belirtmek için kullanılır.
🧠 Polymorphism	Farklı alt sınıflar aynı metodu farklı şekilde çalıştırabilir.

 Overriding ≠ Overloading

Özellik	Overriding	Overloading
Miras gerekli mi?	Evet	Hayır
İsim aynı mı?	Evet	Evet
Parametre farkı?	Hayır	Evet (sayı veya tip farklı)
Amaç	Davranışı değiştirmek	Farklı şekillerde aynı işi yapmak
#salesforce
Salesforce Apex’te Overriding:

public virtual class Hayvan {
    public virtual void sesCikar() {
        System.debug('Hayvan sesi');
    }
}

public class Kedi extends Hayvan {
    public override void sesCikar() {
        System.debug('Miyav!');
    }
}


class Hayvan:
    def ses_cikar(self):
        print("Bir hayvan ses çıkarıyor")


class Kedi(Hayvan):
    def ses_cikar(self):  # Override ediyoruz
        print("Miyav!")


class Kopek(Hayvan):
    def ses_cikar(self):  # Override ediyoruz
        print("Hav hav!")


# Kullanım
hayvan = Hayvan()
kedi = Kedi()
kopek = Kopek()

hayvan.ses_cikar()  # Bir hayvan ses çıkarıyor
kedi.ses_cikar()  # Miyav!
kopek.ses_cikar()  # Hav hav!

#super() ile Üst Sınıf Metoduna Erişim:

class Kedi(Hayvan):
    def ses_cikar(self):
        super().ses_cikar()  # Üst sınıftaki metodu çağır
        print("Miyav!")

        k = Kedi()
        k.ses_cikar()
Overriding Ne İşe Yarar?
Ortak bir interface (arayüz) tanımlayıp alt sınıfların davranışlarını özelleştirmeye yarar.

Polymorphism (çok biçimlilik) sağlar.

Kod tekrarını azaltır.

class Arac:
    def calistir(self):
        print("Araç çalıştı")

class Araba(Arac):
    def calistir(self):
        print("Araba motoru çalıştı")

class ElektrikliAraba(Araba):
    def calistir(self):
        print("Sessizce elektrikli araba çalıştı")
for arac in [Arac(), Araba(), ElektrikliAraba()]:
    arac.calistir()


#Tkinter + OOP + Overriding
import tkinter as tk

# Üst sınıf (Base Window)
class AnaPencere:
    def __init__(self, baslik="Ana Pencere"):
        self.pencere = tk.Tk()
        self.pencere.title(baslik)
        self.etiket = tk.Label(self.pencere, text="Merhaba, ben ana pencere.")
        self.etiket.pack(padx=20, pady=20)
        self.dugme = tk.Button(self.pencere, text="Kapat", command=self.kapat)
        self.dugme.pack()

    def kapat(self):
        print("Pencere kapatılıyor...")
        self.pencere.destroy()

    def baslat(self):
        self.pencere.mainloop()
#Overriding Yapan Alt Sınıf

class OzellestirilmisPencere(AnaPencere):
    def __init__(self):
        super().__init__(baslik="Özel Pencere")  # override: farklı başlık

        # Override: Etiketi güncelle
        self.etiket.config(text="Bu özel bir pencere!")

        # Override: Yeni buton ekle
        self.yeni_dugme = tk.Button(self.pencere, text="Merhaba de", command=self.merhaba_de)
        self.yeni_dugme.pack()

    # Override: Yeni bir metod
    def merhaba_de(self):
        print("Merhaba! Bu özel bir pencere.")

    # Override: kapat() metodunu özelleştir
    def kapat(self):
        print("Özel pencere kapatılıyor...")
        super().kapat()
# Ana pencereyi açmak istersen:
# pencere = AnaPencere()

# Override edilmiş pencereyi aç:
pencere = OzellestirilmisPencere()
pencere.baslat()
Neyi Override Ettik?

Metot / Özellik	Nerede?	Ne Yaptık?
__init__	OzellestirilmisPencere	     Başlığı ve etiket metnini değiştirdik
kapat()	OzellestirilmisPencere       	 Kapatma davranışını özelleştirdik
merhaba_de()	Yeni metot           	 Ekstra işlev ekledik

"""