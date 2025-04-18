"""6. Python Bellek Yönetimi Derinlemesine
6.1 Nesnelerin Yaşam Döngüsü
Python('da bir nesnenin yaşam döngüsü, referans sayımı ve çöp toplama ile yönetilir.'
       ' Nesneler oluşturulduğunda, Python bunlara referans sayısı atar.'
       ' Bu referans sayısı sıfırlandığında, nesne çöp toplama için uygun hale gelir. '
       'Çöp toplama, nesneye başkası tarafından referans verilmediği zaman aktif hale gelir.)

Bununla birlikte, Python('da bazı nesneler için özel bellek yönetimi stratejileri vardır.'
                         ' Örneğin, bazı yerleşik veri tipleri (liste, sözlük gibi) ve kullanıcı tanımlı sınıflar (class) kendi bellek yönetim tekniklerine sahip olabilir.)

6.2 Python Nesnelerinin Çöp Toplama ve Referans Sayımı
Python('da bir nesnenin ne zaman bellekten silineceğini belirlemek,'
       ' referans sayımının sıfırlanması ve çöp toplama mekanizmalarına bağlıdır.'
       ' Nesnelerin yaşam döngüsü, genellikle şu şekilde işler:)

Bir nesne yaratıldığında, Python onun için bellek ayırır.

Bu nesneye her yeni referans verildiğinde, referans sayısı artar.

Bir referans nesneden silindiğinde, referans sayısı azalır.

Bir nesnenin referans sayısı sıfırlandığında, çöp toplama mekanizması bu nesneyi bellekten temizler.

Eğer nesne döngüsel referansa sahipse, çöp toplama algoritması devreye girer ve nesneyi temizler.

Python('da çöp toplama için kullanılan temel yöntem,'
       ' referans sayımının sıfırlanması ve döngüsel referansların temizlenmesi üzerinedir.'
       ' Ancak, referans sayımı ve çöp toplama yalnızca nesnelerin bellekten serbest bırakılmasını sağlar. Nesnelerin yeniden kullanılabilir olması için Python,'
       ' bellek havuzlarını kullanarak bellek yönetimini daha verimli hale getirir.)

6.3 Bellek Havuzları (Memory Pools)
Python, küçük nesneler için bellek havuzları kullanır.
Bu, bellek tahsis ve serbest bırakma işlemlerini hızlandırarak programın verimliliğini artırır.
Python’un pymalloc adlı içsel bellek yöneticisi, bellek havuzlarıyla çalışarak küçük nesneler için bellek blokları oluşturur. Bu, özellikle kısa ömürlü nesneler için önemli bir optimizasyon tekniğidir.

Python, bellek havuzları üzerinde çalışırken, nesneler için belirli boyut aralıkları kullanır.
Bu sayede, bellek tahsisi ve serbest bırakma işlemleri daha hızlı gerçekleştirilir.

6.4 Çöp Toplama (GC) ve Yaşamakta Olan Nesneler
Python’un çöp toplama algoritması, nesnelerin yaşadığı generations (yongalar) üzerinden çalışır. Bu üç nesne kümesi şu şekilde yönetilir:

Generation 0: Yeni nesneler buradadır. Bu nesneler hızlı bir şekilde yaşlanıp bir üst yongaya geçer.

Generation 1: Generation 0’daki nesneler hayatta kalırsa, Generation 1'e taşınır.

Generation 2: Uzun süre yaşayan nesneler Generation 2'ye taşınır. Python çöp toplama işlemini bu nesneler üzerinde daha seyrek yapar.

Çöp toplama işlemi, Generation 0 üzerindeki nesnelerle daha sık gerçekleştirilir.
Çünkü bu nesnelerin çoğu kısa ömürlüdür.
Eğer bir nesne yaşam süresi uzarsa, bir sonraki generasyona geçer.
Bu, Python'un bellek kullanımını daha verimli hale getirir.

6.5 Çöp Toplama Algoritmalarındaki İyileştirmeler
Python, çöp toplama algoritmasını sürekli iyileştirmiştir.
Bu iyileştirmeler, özellikle nesnelerin yaşam sürelerini daha etkin bir şekilde yönetmeyi amaçlar.
Özellikle döngüsel referanslar ve karmaşık nesne ilişkileri söz konusu olduğunda, Python’un çöp toplama algoritması şu iki başlıca iyileştirmeyi içerir:

Döngüsel referansların tanımlanması ve temizlenmesi:
Python, nesneler arasındaki döngüsel referansları tespit eder ve bunları çöp toplama mekanizmasına dahil eder.

Nesne nesil sistemi: Nesneler, her nesil geçtiğinde çöp toplama sıklığı düşer.
Bu sistem, daha önce yaşamış nesnelerin daha az sıklıkta temizlenmesini sağlar.

7. Python Bellek Optimizasyonu
7.1 Bellek Profilleme
Python’da bellek kullanımını optimize etmek için kullanılan bazı araçlar vardır.
Bu araçlar, programınızın hangi kısımlarının fazla bellek kullandığını tespit etmenize yardımcı olabilir. Aşağıdaki araçlar Python’da bellek profilini çıkarmak için yaygın olarak kullanılır:

memory_profiler: Python programlarının bellek kullanımını satır satır izler. Bu araç, hangi fonksiyonların ne kadar bellek kullandığını gösterebilir.

bash
pip install memory_profiler
from memory_profiler import profile

@profile
def my_function():
    a = [1] * (10**6)  # Bellek kullanan işlem
    b = [2] * (2 * 10**7)
    del b
    return a

if __name__ == "__main__":
    my_function()
objgraph: Bu araç, Python nesneleri arasındaki ilişkileri ve referansları görselleştirir.
Bellek sızıntıları ve döngüsel referanslar hakkında bilgi verir.

pip install objgraph

import objgraph
objgraph.show_most_common_types()
7.2 Bellek Sızıntılarını Önlemek
Bellek sızıntıları genellikle iki ana nedenden kaynaklanır:

Döngüsel referanslar: Çöp toplama, döngüsel referanslar nedeniyle nesneleri serbest bırakamayabilir.
Bu tür sorunları engellemek için, nesneler arasındaki ilişkileri dikkatlice yönetmek gereklidir.

Kapanmamış kaynaklar: Dosyalar, ağ bağlantıları veya veritabanı bağlantıları gibi kaynaklar açık bırakıldığında bellek sızıntılarına yol açabilir. Bu nedenle, with yapıları ve try-finally blokları ile kaynakların düzgün bir şekilde kapanması sağlanmalıdır.

7.3 Optimizasyon Teknikleri
__slots__ Kullanımı: Python’daki her sınıf bir __dict__ içeren bir nesne oluşturur.
Ancak, __slots__ özelliği ile bu __dict__'i devre dışı bırakabilir ve daha az bellek kullanabilirsiniz. Bu, büyük sayıda nesne oluşturduğunuzda önemli bir optimizasyon sağlar.

python
Kopyala
Düzenle
class MyClass:
    __slots__ = ['name', 'age']  # __dict__ yerine bu iki alan tanımlanır
    def __init__(self, name, age):
        self.name = name
        self.age = age
Zayıf Referanslar: Büyük veri yapıları ile çalışırken, weakref kullanarak bellek üzerinde daha fazla kontrol sahibi olabilirsiniz. Bu sayede, nesneler gereksiz yere bellekten silinmeden önce, Python'un çöp toplama algoritması devreye girebilir.

"""