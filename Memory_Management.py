"""1. Python Bellek Yönetimi Temelleri
Python, otomatik bellek yönetimi ve çöp toplama (garbage collection) ile tanınır.
Yani, Python programı çalışırken bellek tahsisi ve serbest bırakma işlemleri genellikle Python tarafından yönetilir.

1.1 Bellek Tahsisi
Python’da bellek tahsisi, genellikle bir nesne oluşturulduğunda yapılır.
Python, nesneler için bellek tahsis eder ve bu nesnelerin yaşam döngüsünü yönetir.
Python’da veri türleri (int, str, list, vb.)
aslında bir nesne olduğundan, bunların her biri bellekte bir alan kaplar.

Python('un bellek havuzu (memory pool) sistemi, nesnelerin yaratılması için hız sağlar. '
       'Küçük nesneler için, Python önceden tahsis edilmiş bellek bloklarını kullanabilir. '
       'Bu, bellek kullanımını optimize eder.)

1.2 Bellek Yönetimi ve Refereans Sayımı
Python, referans sayımı (reference counting) adı verilen bir mekanizmayı kullanarak nesnelerin yaşam döngülerini yönetir.
Bir nesne oluşturulduğunda, ona bir referans sayısı atanır.
Bu referans sayısı, nesneye referans veren değişkenlerin sayısına bağlıdır.

Herhangi bir nesne, referans sayısı sıfır olduğunda,
yani artık ona referans veren hiçbir değişken kalmadığında Python,
bu nesneyi çöp toplama mekanizması aracılığıyla bellekten temizler.
Bu, Python’un bellek yönetimi için en temel mekanizmadır.

2. Python Çöp Toplama (Garbage Collection)
2.1 Çöp Toplama Nedir?
Çöp toplama, kullanılmayan ve belleği israf eden nesnelerin otomatik olarak serbest bırakılması işlemidir.
Python’da, nesnelerin yaşam süresi referans sayımı ile takip edilse de,
çöp toplama işlevi, döngüsel referanslar gibi karmaşık durumları yönetmek için devreye girer.

2.2 Döngüsel Referanslar (Circular References)
Bir nesne, başka bir nesneye referans veriyorsa ve bu ikinci nesne ilk nesneye geri referans veriyorsa,
bu döngüsel referans olarak adlandırılır.
Bu durumda, her iki nesne de birbirini referans verdiğinden,
referans sayımları sıfır olamaz. Bu tür durumlar, bellek sızıntılarına yol açabilir.

Python, döngüsel referansları çöp toplama ile temizler.
Python('un çöp toplama mekanizması, referans sayımlarına ek olarak,'
       ' döngüsel referansları tespit etmek için daha gelişmiş bir algoritma kullanır.)

2.3 Çöp Toplama Algoritması
Python’da çöp toplama, genel çöp toplama algoritması kullanılarak yapılır.
Bu algoritma, nesneleri üç yongaya (generations) ayırır:

Generation 0: Yeni oluşturulan nesneler burada yer alır.

Generation 1: Generation 0’da kalan nesneler bir sonraki seviyeye taşınır.

Generation 2: Uzun süre yaşamış nesneler buraya taşınır.

Bu yapı, çöp toplamanın etkinliğini artırır. Çünkü, Python,
nesnelerin çoğunun kısa ömürlü olduğunu varsayar ve bu nedenle
çöp toplama işlemini daha sık Generation 0 üzerinde yapar.
Eğer bir nesne hayatta kalırsa, bir üst generation’a taşınır.

2.4 Çöp Toplamayı Kontrol Etme
Python, çöp toplama işlemlerini otomatik olarak yapar,
ancak geliştiriciler çöp toplama işlemini manuel olarak da kontrol edebilirler. Bunun için gc modülü kullanılır:

import gc

# Çöp toplama işlemini manuel olarak başlatma
gc.collect()

# Çöp toplama durumu hakkında bilgi
print(gc.get_count())


3. Python Bellek Yönetimi Araçları
3.1 sys Modülü
Python, bellek kullanımını izlemek için sys modülünü sunar.
Bu modülde, bellek hakkında bilgi veren çeşitli fonksiyonlar bulunmaktadır:

import sys

# Bir nesnenin bellek kullanımını öğrenme
obj = []
print(sys.getsizeof(obj))  # obj nesnesinin bellekte kapladığı alan


3.2 weakref Modülü
weakref modülü, zayıf referanslar oluşturmanıza olanak tanır.
Zayıf referanslar, bir nesneyi referans gösterir ancak
çöp toplama sırasında bu nesneyi korumaz. Bu özellik,
özellikle büyük veritabanı nesnelerinin bellekten temizlenmesi gerektiğinde kullanışlıdır.

import weakref

class MyClass:
    pass

obj = MyClass()
weak_ref = weakref.ref(obj)

# Nesneye referans
print(weak_ref())  # obj’ye zayıf referans
4. Bellek Sızıntıları ve Optimizasyon
Python’da bellek sızıntıları, çoğunlukla döngüsel referanslar veya nesnelerin gereksiz yere bellekte tutulmasından kaynaklanır.
Çöp toplama bu tür sızıntıları engellemeye yardımcı olur,
ancak yine de bazı durumlarda geliştiricinin dikkatli olması gerekebilir.

4.1 Bellek Sızıntıları Nasıl Tespit Edilir?
Python, bellek sızıntılarını tespit etmek için objgraph gibi kütüphaneleri kullanabilir.
Bu tür kütüphaneler, nesnelerin referans ağlarını görsel olarak analiz etmenize olanak sağlar.

4.2 Bellek Yönetimi İpuçları
Nesneleri yeniden kullanın: Gereksiz nesne oluşturmayı engellemek için nesneleri yeniden kullanmak bellek kullanımını optimize eder.

Zayıf referansları kullanın: Bellekteki büyük nesneleri yönetirken zayıf referansları kullanarak bellek sızıntılarını azaltabilirsiniz.

Profiling araçları kullanın: memory_profiler gibi araçlarla bellek kullanımını izleyerek hangi bölümlerde fazla bellek kullanıldığını analiz edebilirsiniz.

5. Sonuç
Python’un bellek yönetimi, çoğunlukla otomatik olmasına rağmen,
geliştiricilerin bazı durumları anlaması ve optimizasyon yapması önemlidir.
Referans sayımı ve çöp toplama gibi mekanizmalar, Python’un bellek yönetimini güçlü kılar,
ancak döngüsel referanslar ve bellek sızıntıları gibi sorunlarla karşılaşmamak için dikkatli olunması gerekir
.6.
Python Bellek Yönetimi Derinlemesine
6.1 Nesnelerin Yaşam Döngüsü
Python('da bir nesnenin yaşam döngüsü, referans sayımı ve çöp toplama ile yönetilir.'
       ' Nesneler oluşturulduğunda, Python bunlara referans sayısı atar. '
       'Bu referans sayısı sıfırlandığında, nesne çöp toplama için uygun hale gelir. '
       'Çöp toplama, nesneye başkası tarafından referans verilmediği zaman aktif hale gelir.)

Bununla birlikte, Python('da bazı nesneler için özel bellek yönetimi stratejileri vardır. '
                         'Örneğin, bazı yerleşik veri tipleri (liste, sözlük gibi) ve kullanıcı tanımlı sınıflar (class) kendi bellek yönetim tekniklerine sahip olabilir.)

6.2 Python Nesnelerinin Çöp Toplama ve Referans Sayımı
Python('da bir nesnenin ne zaman bellekten silineceğini belirlemek, '
       'referans sayımının sıfırlanması ve çöp toplama mekanizmalarına bağlıdır. '
       'Nesnelerin yaşam döngüsü, genellikle şu şekilde işler:)

Bir nesne yaratıldığında, Python onun için bellek ayırır.

Bu nesneye her yeni referans verildiğinde, referans sayısı artar.

Bir referans nesneden silindiğinde, referans sayısı azalır.

Bir nesnenin referans sayısı sıfırlandığında, çöp toplama mekanizması bu nesneyi bellekten temizler.

Eğer nesne döngüsel referansa sahipse, çöp toplama algoritması devreye girer ve nesneyi temizler.

Python('da çöp toplama için kullanılan temel yöntem,'
       ' referans sayımının sıfırlanması ve döngüsel referansların temizlenmesi üzerinedir.'
       ' Ancak, referans sayımı ve çöp toplama yalnızca nesnelerin bellekten serbest bırakılmasını sağlar. '
       'Nesnelerin yeniden kullanılabilir olması için Python,'
       ' bellek havuzlarını kullanarak bellek yönetimini daha verimli hale getirir.)

6.3 Bellek Havuzları (Memory Pools)
Python, küçük nesneler için bellek havuzları kullanır.
Bu, bellek tahsis ve serbest bırakma işlemlerini hızlandırarak programın verimliliğini artırır.
Python’un pymalloc adlı içsel bellek yöneticisi, bellek havuzlarıyla çalışarak küçük nesneler için bellek blokları oluşturur.
Bu, özellikle kısa ömürlü nesneler için önemli bir optimizasyon tekniğidir.

Python, bellek havuzları üzerinde çalışırken,
nesneler için belirli boyut aralıkları kullanır.
Bu sayede, bellek tahsisi ve serbest bırakma işlemleri daha hızlı gerçekleştirilir.

6.4 Çöp Toplama (GC) ve Yaşamakta Olan Nesneler
Python’un çöp toplama algoritması, nesnelerin yaşadığı generations (yongalar) üzerinden çalışır.
Bu üç nesne kümesi şu şekilde yönetilir:

Generation 0: Yeni nesneler buradadır.
Bu nesneler hızlı bir şekilde yaşlanıp bir üst yongaya geçer.

Generation 1: Generation 0’daki nesneler hayatta kalırsa, Generation 1'e taşınır.

Generation 2: Uzun süre yaşayan nesneler Generation 2('ye taşınır.'
 Python çöp toplama işlemini bu nesneler üzerinde daha seyrek yapar.)

Çöp toplama işlemi, Generation 0 üzerindeki nesnelerle daha sık gerçekleştirilir.
Çünkü bu nesnelerin çoğu kısa ömürlüdür. Eğer bir nesne yaşam süresi uzarsa,
bir sonraki generasyona geçer. Bu, Python'un bellek kullanımını daha verimli hale getirir.

6.5 Çöp Toplama Algoritmalarındaki İyileştirmeler
Python, çöp toplama algoritmasını sürekli iyileştirmiştir.
Bu iyileştirmeler, özellikle nesnelerin yaşam sürelerini daha etkin bir şekilde yönetmeyi amaçlar.
Özellikle döngüsel referanslar ve karmaşık nesne ilişkileri söz konusu olduğunda,
Python’un çöp toplama algoritması şu iki başlıca iyileştirmeyi içerir:

Döngüsel referansların tanımlanması ve temizlenmesi:
Python, nesneler arasındaki döngüsel referansları tespit eder ve bunları çöp toplama mekanizmasına dahil eder.

Nesne nesil sistemi: Nesneler, her nesil geçtiğinde çöp toplama sıklığı düşer.
Bu sistem, daha önce yaşamış nesnelerin daha az sıklıkta temizlenmesini sağlar.

7. Python Bellek Optimizasyonu
7.1 Bellek Profilleme
Python’da bellek kullanımını optimize etmek için kullanılan bazı araçlar vardır.
Bu araçlar, programınızın hangi kısımlarının fazla bellek kullandığını tespit etmenize yardımcı olabilir.
Aşağıdaki araçlar Python’da bellek profilini çıkarmak için yaygın olarak kullanılır:

memory_profiler: Python programlarının bellek kullanımını satır satır izler.
Bu araç, hangi fonksiyonların ne kadar bellek kullandığını gösterebilir.



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


class MyClass:
    __slots__ = ['name', 'age']  # __dict__ yerine bu iki alan tanımlanır
    def __init__(self, name, age):
        self.name = name
        self.age = age
Zayıf Referanslar: Büyük veri yapıları ile çalışırken, weakref kullanarak bellek üzerinde daha fazla kontrol sahibi olabilirsiniz. Bu sayede, nesneler gereksiz yere bellekten silinmeden önce, Python'un çöp toplama algoritması devreye girebilir.
"""