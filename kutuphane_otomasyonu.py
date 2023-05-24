from abc import ABC, abstractmethod
# Kütüphane base, Giriş child class. Bu classlarda polymorphism yapılmıştır.
class Kütüphane(ABC):
    @abstractmethod
    def __init__(self, kullanıcı_adi, parola):
        self.kullanıcı_adi = kullanıcı_adi
        self.parola = parola

    @abstractmethod
    def kullanıcı_ekle(self):
        pass

    @abstractmethod
    def get_kullanıcı_bilgi_goster(self):
        pass

    @abstractmethod
    def set_kullanıcı_bilgi_goster(self):
        pass

# Giriş sayfasında kullanıcı adı, şifre girilmektedir.   
class Giris(Kütüphane):
    def __init__(self, kullanıcı_adi, parola):
        super().__init__(kullanıcı_adi, parola)
        self.__kullanıcı_bilgileri = {}

    #Kullanıcı adı ve şifrelerini kullanıcı_bilgileri sözlüğünde tutuyoruz.
    def kullanıcı_ekle(self):
        self.__kullanıcı_bilgileri= {
            "Kullanıcı Adı" : self.kullanıcı_adi,
            "Parola": self.parola
        }

    #kullanıcı_bilgileri sözlüğünü geri dönderme işlemi yapılıyor.
    def get_kullanıcı_bilgi_goster(self):
        return self.__kullanıcı_bilgileri

    #kullanıcı_bilgileri sözlüğünü ekranda yazdırma işlemi yapılıyor
    def set_kullanıcı_bilgi_goster(self):
        print(self.__kullanıcı_bilgileri)   

# Üye base, Akademisyen ve Ogrenci child class. Bu classlarda üye bilgileri alınmaktadır.
class Üye(ABC):
    @abstractmethod
    def __init__(self, isim, soyisim, bolum):
        self.isim = isim
        self.soyisim = soyisim
        self.bolum = bolum
        
    @abstractmethod
    def id_duzenle(self):
        pass

# Akademisyen nesnesi oluşturacak class tanımlanmıstır.
class Akademisyen(Üye):
    # Class metot için kurum değişkeni tanımlanmıştır.
    kurum = "Hitit Üniversitesi"
    def __init__(self, id, isim, soyisim, bolum, unvan):
        super().__init__(isim, soyisim, bolum)
        self.unvan = unvan
        self.id = id
        self.__akademisyen_bilgileri = {}
    
    #Oluşturulan akademisyen nesnesinin bilgileri akademisyen_bilgileri adında sözcukte tutulmaktadır.
    def akademisyen_bilgileri(self):
        self.__akademisyen_bilgileri = {
            "id" : self.id,
            "İsim": self.isim,
            "Soyisim": self.soyisim,
            "Bolum": self.bolum,
            "Unvan":self.unvan
        }
    
    #Oluşturulan akademisyen nesnesinin id güncellemesi yapılmaktadır.
    def id_duzenle(self,yeni_id):
        self.id = yeni_id

    #Class method ile kurum ekrana yazdırdık.
    @classmethod
    def kurumadi(cls):
        print(cls.kurum)

    #Statik method ile kullanıcı akademisyeni seçerse hangi bilgilerin gireceğini belirttim.
    @staticmethod
    def akademisyen_bilgisi():
        print("Akademisyen seçilirse id, isim, isoyisim, bölüm, ünvan bilgileri istenecektir.")

    #__akademisyen_bilgileri sözlüğünü geri dönderme işlemi yaptım.
    def get_akademisyen_listesi(self):
        return self.__akademisyen_bilgileri

#Öğrenci nesnesi oluşturacak class tanımlanmıstır.
class Ogrenci(Üye):
    # Class metot için kurum değişkeni tanımlanmıştır.
    kurum = "Hitit Üniversitesi"
    def __init__(self, id, isim, soyisim, bolum, sınıf):
        super().__init__(isim, soyisim, bolum)
        self.sınıf = sınıf
        self.id = id
        self.__ogrenci_bilgileri = {}

    #Oluşturulan öğrenci nesnesinin bilgileri __ogrenci_bilgileri adında sözcukte tutulmaktadır.
    def ogrenci_bilgi(self):
        self.__ogrenci_bilgileri = {
            "id" : self.id,
            "İsim": self.isim,
            "Soyisim": self.soyisim,
            "Bolum": self.bolum,
            "Sınıf":self.sınıf
        }

    #Class method ile kurum adını ekrana yazdırdık.
    @classmethod
    def kurumadi(cls):
        print(cls.kurum)

    #Statik method ile kullanıcı öğrenciyi seçerse hangi bilgilerin gireceğini belirttim.
    @staticmethod
    def ogrenci_bilgisi():
        print("Öğrenci seçilirse id, isim, soyisim, bölüm, sınıf bilgileri istenecektir.")
    
    # Kullanıcı girilen öğrencinin id düzenlemesini yapabilecektir.
    def id_duzenle(self,yeni_id):
        self.id = yeni_id

    #__ogrenci_bilgileri sözlüğünü ekrana yazdırma işlemi yaptım.
    def set_ogrenci_listesi(self):
        print(self.__ogrenci_bilgileri)

    #__ogrenci_bilgileri sözlüğünü geri dönderme işlemi yaptım.
    def get_ogrenci_listesi(self):
        return self.__ogrenci_bilgileri

# İçerikler base, Makale, Sözlük, Kitap child class. Bu classlarda kitap,makale,sözlük işlemleri yapılmaktadır.
class İçerikler(ABC):
    #içerikler classında 3 türde(makale,kitap,dergi)bulunan ortak değerler
    @abstractmethod
    def __init__(self, isim, yazar, sayfa_sayisi):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
    #İçeriklerin herhangi birinin ismi getirilecektir. (Kitap,Sözlük,Makale)
    @abstractmethod
    def get_isim(self):
        pass

#Makale nesnesi oluşturulacak class tanımlanmıştır.
class Makale(İçerikler):
    #Nesne oluşturulacak özellikler girilecektir. isim,yazar ve sayfa sayısı içerikler classından kalıtım olarak alınmıştır.
    def __init__(self, isim, yazar, sayfa_sayisi, alan):
        super().__init__(isim, yazar, sayfa_sayisi)
        self.alan = alan
        self.__makale_bilgileri = {}

    #__makale_bilgileri sözlüğüne makale bilgileri yazdırılmıştır.
    def makale_bilgi(self):
        self.__makale_bilgileri = {
            "İsim": self.isim,
            "Yazar": self.yazar,
            "Alan": self.alan,
            "Sayfa Sayisi": self.sayfa_sayisi,
        }

    #__makale_bilgileri sözlüğünü ekrana yazdırma işlemi yapılacaktır.
    def set_makale_bilgi(self):
        print(self.__makale_bilgileri)

    #__makale_bilgileri sözlüğünü geri dönderme işlemi yapılacaktır.
    def get_makale_bilgi(self):
        return self.__makale_bilgileri

    #Makale ismi geri dönderme işlemi yapılacaktır.
    def get_isim(self):
        return self.isim

#Sözlük nesnesi oluşturulacak class tanımlanmıştır.
class Sozluk(İçerikler):
    def __init__(self, isim, yazar, sayfa_sayisi, dil):
        super().__init__(isim, yazar, sayfa_sayisi)
        self.dil = dil
        self.__sozluk_bilgileri = {}

    #sözlükte ek parametre olarak dil eklendi. __sozluk_bilgileri sözlüğüne girilen nesne özellikleri atandı.
    def sozluk_bilgi(self):
        self.__sozluk_bilgileri = {
            "isim": self.isim,
            "yazar": self.yazar,
            "dil": self.dil,
            "sayfa_sayisi": self.sayfa_sayisi,
        }

    #__sozluk_bilgileri sözlüğündeki bilgileri ekrana yazdıracak
    def set_sozluk_bilgi(self):
        print(self.__sozluk_bilgileri)

    #__sozluk_bilgileri sözlüğündeki bilgileri geri dönderme işlem yapıldı.
    def get_sozluk_bilgi(self):
        return self.__sozluk_bilgileri

    #Sözlük ismini geri dönderme işlemi yapıldı.
    def get_isim(self):
        return self.isim

#Sözlük nesnesi oluşturulacak class tanımlanmıştır.
class Kitap(İçerikler):
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        super().__init__(isim, yazar, sayfa_sayisi)
        self.tur = tur
        self.__kitap_bilgileri = {}

    #kitapta ek parametre olarak bu seferde tür ekledik. Nesnesi oluşturulan kitap bilgileri, __kitap_bilgileri sözlüğüne atama işlemii yapıldı.
    def kitap_bilgi(self):
        self.__kitap_bilgileri = {
            "isim": self.isim,
            "yazar": self.yazar,
            "Tur": self.tur,
            "sayfa_sayisi": self.sayfa_sayisi,
        }

    #__kitap_bilgileri ekrana yazdırma işlemi yapılmıştır.
    def set_kitap_bilgi(self):
        print(self.__kitap_bilgileri)

    #__kitap_bilgileri geri döndürme işlemi yapılmıştır.
    def get_kitap_bilgi(self):
        return self.__kitap_bilgileri

    # Kitap ismi getirilecektir.
    def get_isim(self):
        return self.isim


# Boş listeler tanımladım, oluşturulan nesnelerin bilgileri tutulacaktır. 
kullanıcı_adi_listesi = []
parola_listesi = []
akademisyen_listesi = []
Ogrenci_listesi = []
uye_id = []
makale_listesi = []
sozluk_listesi = []
kitap_listesi = []

# Anahtar = 1 değeri oldukca aşağıdaki while döngüleri dönecektir.
anahtar = 1

# Kütüphane girişindeki temel işlemler yapılmaktadır. Kayıt oluştur,Giriş yap..
while anahtar == 1:
    print("\nKütüphanemize Hoş Geldiniz... \n *********************************")
    islem = input("Giriş Yapmak için (1), Üye Olmak İçin (2), Çıkış yapmak için(q) : ")
    
    if islem == "q":
        print("çıkılıyor...")
        anahtar = 0

    #Giriş yapılırken kullanıcı adi ve şifresi sorgulama işlemi yapılmaktadır.
    elif islem == "1":
        kullaniciadi = input("Lütfen Kullanıcı Adınızı Giriniz:")
        parola = input("Lütfen Parolanızı Giriniz:")
        if kullaniciadi in kullanıcı_adi_listesi and parola in parola_listesi:
            print("Giriş Yaptınız")
            anahtar = 0
        else:
            print("Yanlıs kullanıcı adı veya şifre..(Büyük-Küçük Harf Duyarlıdır.)")

    #Kayıt oluşturulma kısmı
    elif islem == "2":
        kayıt_kullaniciadi = input("Lütfen Kullanıcı Adınızı Giriniz:")
        kayıt_parola = input("Lütfen Parolanızı Giriniz:")
        k1 = Giris(kayıt_kullaniciadi,kayıt_parola)
        k1.kullanıcı_ekle() #k1 sözlüğü oluşturdum. 
        kullanıcı_adi_listesi.append(k1.get_kullanıcı_bilgi_goster()['Kullanıcı Adı']) #Oluşturulan sözlükten kullanıcı adı kullanıcı_adi_listesine eklenmektedir.
        parola_listesi.append(k1.get_kullanıcı_bilgi_goster()['Parola']) #Aynı işlemin parolası yapılır.
        print("Kayıt İşleminiz Başarılı...")

# Yukarıda anahtar = 1 yapmamızın sebebi yukarıdaki while döngüsünde anahtar = 0 kalmıştı.
anahtar = 1
# Aşağıdaki while döngüsünde Üye İşlemleri yapılmaktadır.
while anahtar == 1:
    print("\n Hoş Geldin... \n *********************************")
    nesiniz = input("Akademisyen iseniz(1), Öğrenci İseniz(2), Akademisyen Listele(3), Öğrenci Listele(4) Uye İd Sırala(5) Çıkış İçin(6) Üye Silmek İçin(7) İd Düzenle(8) Kullanıcı ekleme bilgileri (9) Kurum Bilgisi(10): ")

    #Akademisyen nesnesi oluşturulur.
    if nesiniz == "1":
        a_id = input("İd Giriniz:")
        a_isim = input("İsim Giriniz:")
        a_soyisim = input("Soyisim Giriniz:")
        a_bolum = input("Bolum Giriniz:")
        a_unvan = input("unvan Giriniz:")
        a1 = Akademisyen(a_id,a_isim,a_soyisim,a_bolum,a_unvan)
        a1.akademisyen_bilgileri() #Akademisyen sözlüğü oluşturuldu.
        akademisyen_listesi.append(a1.get_akademisyen_listesi()) #Akademisyen sözlüğünü akademisyen listesine ekledim.
        uye_id.append(a1.get_akademisyen_listesi()['id']) #Akademisyen id'sini uye_id'ne ekledim.
        print("Akademisyen Eklendi")

    #Öğrenci nesnesi oluşturulur.
    if nesiniz == "2":
        o_id = input("İd Giriniz:")
        o_isim = input("İsim Giriniz:")
        o_soyisim = input("Soyisim Giriniz:")
        o_bolum = input("Bolum Giriniz:")
        o_sınıf = input("Sınıf Giriniz:")
        o1 = Ogrenci(o_id, o_isim, o_soyisim, o_bolum, o_sınıf)
        o1.ogrenci_bilgi()
        Ogrenci_listesi.append(o1.get_ogrenci_listesi())
        uye_id.append(o1.get_ogrenci_listesi()['id'])
        print("Öğrenci Eklendi")

    elif nesiniz == "3":
        print(akademisyen_listesi)

    elif nesiniz == "4":
        print(Ogrenci_listesi)

    elif nesiniz == "5":
        print(uye_id)
    
    elif nesiniz == "6":
        anahtar = 0
    
    # Üye silme işlemleri yapılır. uye_id listesinden ve akademisyen veya ogrenci listesinden de silme yapılır.
    elif nesiniz == "7":
        sil_id = input("Silmek İstediğiniz Üye İD :")
        silinecek_uye = input("Akademisyen(1) Öğrenci(2) : ")
        
        if silinecek_uye == "1":
            akademisyen_listesi.pop()
            if sil_id in uye_id:
                uye_id.remove(sil_id)
                print("Üye Tamamen Silindi")

        elif silinecek_uye == "2":
            Ogrenci_listesi.pop()
            if sil_id in uye_id:
                uye_id.remove(sil_id)
                print("Üye Tamamen Silindi")
        
        else:
            print("Yanlış Değer Girdiniz...")

    # İD güncellemesi yapılır.
    elif nesiniz == "8":
        degisecek_id = input("Değiştirilecek Id : ")
        guncelle_secim = input("İd değiştirilecek Akademisyen(1) Öğrenci(2) :")
        yeni_id = input("Yeni id giriniz : ")
        if guncelle_secim == "1":
            a1.id_duzenle(yeni_id)
            if degisecek_id in uye_id:
                uye_id.remove(degisecek_id)
                uye_id.append(yeni_id)
                print("Akademisyen İD değiştirildi..")
        elif guncelle_secim == "2":
            o1.id_duzenle(yeni_id)
            if degisecek_id in uye_id:
                uye_id.remove(degisecek_id)
                uye_id.append(yeni_id)
                print("Öğrenci İD değiştirildi..")
        else:
            print("Yanlış sayı girdiniz...")
    
    #Statik metot ile bilgi getirme işlemi yapıldı.
    elif nesiniz == "9":
        hangi_bilgi = input("Bilgisini almak istediğiniz kategori? Akademisyen(1) Öğrenci(2) : ")
        if hangi_bilgi == "1":
            a1.akademisyen_bilgisi()
        elif hangi_bilgi == "2":
            o1.ogrenci_bilgisi()
        else:
            print("Yanlış Tuşlama...")
    # Kurum adını class metot ile çağırdık.
    elif nesiniz == "10":
        print("Kurum adını öğrenebilmek için akademisyen veya öğrenci nesnesi oluşturulmalıdır.")
        kurumadi = input("Kimin kurum adını öğrenmek istiyorsunuz A(1) Ö(2) : ")
        if kurumadi == "1":
            a1.kurumadi()
        elif kurumadi == "2":
            o1.kurumadi()
        else:
            print("Hatalı tuşlama")

anahtar = 1

# Aşağıdaki while döngüsüyle İçerik İşlemleri yapılmaktadır.
while anahtar == 1:
    print("\n İçerikler Kısmına Hoş Geldin... \n *********************************")
    nesiniz = input("Makale(1), Sözlük(2), Kitap(3), Makale Listele(4) Sözlükleri Listele (5) Kitapları Listele(6) İçerik Silmek İçin (7) İçerik İsmi Getir(8) Çıkış İçin(9): ")

    #Makale Ekleme
    if nesiniz == "1":
        m_isim = input("İsim Giriniz:")
        m_yazar = input("Yazar Giriniz:")
        m_sayfa_sayisi = input("Sayfa Sayisi Giriniz:")
        m_alan = input("Alan Giriniz:")
        m1 = Makale(m_isim, m_yazar, m_sayfa_sayisi, m_alan)
        m1.makale_bilgi()
        makale_listesi.append(m1.get_makale_bilgi())
        print("Makale Eklendi")

    #Sözlük Ekleme
    if nesiniz == "2":
        s_isim = input("İsim Giriniz:")
        s_yazar = input("Yazar Giriniz:")
        s_sayfa_sayisi = input("Sayfa Sayisi Giriniz:")
        s_dil = input("Dil Giriniz:")
        s1 = Sozluk(s_isim, s_yazar, s_sayfa_sayisi, s_dil)
        s1.sozluk_bilgi()
        sozluk_listesi.append(s1.get_sozluk_bilgi())
        print("Sözlük Eklendi")
    
    #Kitap ekleme
    elif nesiniz == "3":
        ki_isim = input("İsim Giriniz:")
        ki_yazar = input("Yazar Giriniz:")
        ki_sayfa_sayisi = input("Sayfa Sayisi Giriniz:")
        ki_tur = input("Tür Giriniz:")
        ki1 = Kitap(ki_isim, ki_yazar, ki_sayfa_sayisi, ki_tur)
        ki1.kitap_bilgi()
        kitap_listesi.append(ki1.get_kitap_bilgi())
        print("Kitap Eklendi")

    #Makale listesi görüntülenir.
    elif nesiniz == "4":
        print(makale_listesi)

    #sozlük listesi görüntülenir.
    elif nesiniz == "5":
        print(sozluk_listesi)

    #kitap listesi görüntülenir.
    elif nesiniz == "6":
        print(kitap_listesi)
    
    #Makale,kitap,sözlük silme işlemleri yapılmaktadır.
    elif nesiniz == "7":
        silinecek_içerik = input("Makale(1) Sözlük(2) Kitap(3) : ")
        
        if silinecek_içerik == "1":
            makale_listesi.pop()
            print("Makale İçerikten Silindi")

        elif silinecek_içerik == "2":
            sozluk_listesi.pop()
            print("Sözlük İçerikten Silindi")
        
        elif silinecek_içerik == "3":
            kitap_listesi.pop()
            print("Kitap İçerikten Silindi")

        else:
            print("Yanlış Değer Girdiniz...")

    # İçeriklere(Makale,Sözlük,Kitap) isimleri getirilmektedir..    
    elif nesiniz =="8":
        mks = input("Hangi Makale(1),Sözlük(2),Kitap(3) İsmini getireceksiniz ? : ")
        if mks == "1":
            print(m1.get_isim())
        elif mks == "2":
            print(s1.get_isim())
        elif mks == "3":
            print(ki1.get_isim())
        else:
            print("Yanlış tuşlama yaptınız...")

    elif nesiniz == "9":
        anahtar = 0
        print("Kütüphaneden Çıkış Yapıldı.")

    else:
        print("Yanlış tuşlama yaptınız...")
