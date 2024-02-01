from abc import ABC, abstractmethod
import random
# Bilgi Üst Sınıf
class HayvanatBahcesi():
    def __init__(self, hayvanat_bahcesi_adi, acilis_yili, bulundugu_sehir, toplam_tur_sayisi):
        self.hayvanat_bahcesi_adi = hayvanat_bahcesi_adi
        self.acilis_yili = acilis_yili
        self.bulundugu_sehir = bulundugu_sehir
        self.toplam_tur_sayisi = toplam_tur_sayisi
         
class Personeller():
    def __init__(self,isim,soyisim,kullanıcıadi,sifre,maas,departman):
        self._isim = isim
        self._soyisim = soyisim
        self._kullanıcıadi = kullanıcıadi
        self._sifre = sifre
        self._maas = maas
        self._departman = departman
    
    def getpersonelkullanıcıadi(self):
        return self._kullanıcıadi
    
    def getpersonelsifre(self):
        return self._sifre
    
    def gorevyap(self):
        print(f"{self._departman} görevini yapmaya gidiyor.")
    
    def personelbilgi(self):
        print(f"{self._isim} {self._soyisim} isimli personelin maası {self._maas} TL'dir.")

#Hayvanlar Üst Sınıfı
class Hayvan(ABC):
    def __init__(self, tur, yas, cins):
        self._tur = tur
        self._yas = yas
        self._cins = cins
    @abstractmethod
    def yemek(self):
        pass
    @abstractmethod
    def uyumak(self): 
        pass
    @abstractmethod
    def hareket_et(self):
        pass 
    @abstractmethod
    def hayvan_bilgi():
        pass     
    
class Aslan(Hayvan):
    def __init__(self, tur, yas, cins,boy,kilo):
        super().__init__(tur, yas, cins)
        self._boy = boy
        self._kilo = kilo
    def yemek(self):
        return f"Aslan avlanıyor"
    def uyumak(self):
        return "Aslan uyuyor"
    def hareket_et(self):
        return "Aslan hareket ediyor"
    def hayvan_bilgi(self):
        print("{0} {1} {2} {3} {4}".format(self._tur,self._yas,self._cins,self._boy,self._kilo))
    
class Yılan(Hayvan):
    def __init__(self, tur, yas, cins, beslenme):
        super().__init__(tur, yas, cins)
        self._beslenme = beslenme
    def yemek(self):
        return f"Aslan avlanıyor: {self._avlanma_davranisi}"
    def uyumak(self):
        return "Yılan uyuyor"
    def hareket_et(self):
        return "Yılan hareket ediyor"
    def hayvan_bilgi(self):
        print("{0} {1} {2} {3}".format(self._tur,self._yas,self._cins,self._beslenme))

class Fil(Hayvan):
    def __init__(self, tur, yas, cins, agirlik="3000-4000 KG"):
        super().__init__(tur, yas, cins)
        self._agirlik = agirlik
    def yemek(self):
        return "Fil yemek yiyor"
    def uyumak(self):
        return "Fil uyuyor"
    def hareket_et(self):
        return "Fil hareket ediyor"
    def agirlik(self):
        return f"Fil ağırlığı : {self._agirlik}" 
    def hayvan_bilgi(self):
        print("{0} {1} {2} {3}".format(self._tur,self._yas,self._cins,self._agirlik))
    
class Penguen(Hayvan):
    def __init__(self, tur, yas, cins, karakteristik_özellikler):
        super().__init__(tur, yas, cins)
        self._karakteristik_özellikler = karakteristik_özellikler
    def yemek(self):
        return "Penguen balık yiyor"
    def uyumak(self):
        return "Penguen uyuyor"
    def hareket_et(self):
        return "Penguen yüzüyor."
    def hayvan_bilgi(self):
        print("{0} {1} {2} {3}".format(self._tur,self._yas,self._cins,self._karakteristik_özellikler))
    
class Papagan(Hayvan):
    def __init__(self, tur, yas, cins, ortalama_ömür):
        super().__init__(tur, yas, cins)
        self._ortalama_omur = ortalama_ömür
    def yemek(self):
        return "Papağan üzüm yiyor"
    def uyumak(self):
        return "Papağan uyuyor"
    def hareket_et(self):
        return "Papağan hareket ediyor"
    def hayvan_bilgi(self):
        print("{0} {1} {2} {3}".format(self._tur,self._yas,self._cins,self._ortalama_omur))
class Maymun(Hayvan): 
    def __init__(self, tur, yas, cins, kilo, boy):
        super().__init__(tur, yas, cins)
        self._kilo = kilo
        self._boy = boy
    def yemek(self):
        return "Maymun muz yiyor"
    def uyumak(self):
        return "Maymun uyuyor"
    def hareket_et(self):
        return "Maymun hareket ediyor"
    def hayvan_bilgi(self):
        print("{0} {1} {2} {3} {4} ".format(self._tur,self._yas,self._cins,self._kilo,self._boy))
class Leopar(Hayvan):
    def __init__(self, tur, yas, cins, ureme ):
        super().__init__(tur, yas, cins)
        self._ureme = ureme
    def yemek(self):
        return "Papağan üzüm yiyor"
    def uyumak(self):
        return "Papağan uyuyor"
    def hareket_et(self):
        return "Papağan hareket ediyor"
    def hayvan_bilgi(self):
        print("{0} {1} {2} {3}".format(self._tur,self._yas,self._cins,self._ureme))
class Zebra(Hayvan):
    def __init__(self, tur, yas, cins, kilo ,ortalama_ömür):
        super().__init__(tur, yas, cins)
        self._ortalama_omur = ortalama_ömür
        self._kilo = kilo
    def yemek(self):
        return "Papağan üzüm yiyor"
    def uyumak(self):
        return "Papağan uyuyor"
    def hareket_et(self):
        return "Papağan hareket ediyor"
    def hayvan_bilgi(self):
        print("{0} {1} {2} {3} {4}".format(self._tur,self._yas,self._cins,self._kilo,self._ortalama_omur))
class Kutup_Ayısı(Hayvan):
    def __init__(self, tur, yas, cins, ureme):
        super().__init__(tur, yas, cins)
        self._ureme = ureme
    def yemek(self):
        return "Papağan üzüm yiyor"
    def uyumak(self):
        return "Papağan uyuyor"
    def hareket_et(self):
        return "Papağan hareket ediyor"
    def hayvan_bilgi(self):
        print("{0} {1} {2} {3}".format(self._tur,self._yas,self._cins,self._ureme))
# Ziyaretçi üst Sınıfı
class Ziyaretci: 
    def __init__(self,ad, soyad, tc, sifre, yas, grup_turu,izlenen_hayvan,kullanıcıadi):
        self._ad = ad
        self._soyad = soyad
        self._tc = tc
        self._yas = yas
        self._sifre = sifre
        self._grup_turu = grup_turu
        self._kullanıcıadi = kullanıcıadi
        self._izlenen_hayvan = izlenen_hayvan
    def getgrup(self):
        return f"{self._ad} {self._grup_turu}"
    def hayvanlari_izle(self):
        print(f"{self._ad} {self._grup_turu} {self._izlenen_hayvan} izliyor")
    def etkilesimde_bulun(self):
        print(f"{self._ad} {self._grup_turu} {self._izlenen_hayvan} etkileşimde bulunuyor")
    def getkullanıcıadi(self):
        return self._kullanıcıadi
    def getsifre(self):
        return self._sifre
       
# Ortam Sınıfı
class Ortam(ABC): 
    def __init__(self, habitat, hayvanlar, cevresel_ozellikler):
        self._habitat = habitat
        self._hayvanlar = hayvanlar
        self._cevresel_ozellikler = cevresel_ozellikler
    def tanit(self):
        return f"{self._cevresel_ozellikler} bölgesindeki ortam"
class Savana(Ortam):
    def __init__(self):
        self._hayvanlar = ["Aslan", "Zebra", "Fil", "Leopar"]
        self._habitat = "Savana Bölgesi"
        self._cevresel_ozellikler = "Kurak ve Yağışlı"
    def gethayvanlar(self):
        return self._hayvanlar
    def tanit(self):
        return super().tanit()
    
class KutupBolgesi(Ortam):
    def __init__(self):
        self._hayvanlar = ["Kutup Ayısı", "Penguen"]
        self._habitat = "Kutup Bölgesi"
        self._cevresel_ozellikler = "Soğuk ve Karlı"
    def gethayvanlar(self):
        return self._hayvanlar
    def tanit(self):
        return super().tanit()
    
class TropikalOrman(Ortam):
    def __init__(self):
        self._hayvanlar = ["Maymun", "Papağan", "Yılan"]
        self._habitat = "Tropikal Ortam"
        self._cevresel_ozellikler = "Sıcak Ve Yağışlı"
    
    def gethayvanlar(self):
        return self._hayvanlar
    
    def tanit(self):
        return super().tanit()

# Günün Zaman Dilimleri Yönetimi
class ZamanYonetimi:
    def __init__(self):
        self.zaman_dilimleri = ["Gece", "Sabah", "Öğle", "Akşam"]

    def zaman_gecir(self):
        suanki_zaman = random.choice(self.zaman_dilimleri)
        print(f"Şu anki zaman dilimi: {suanki_zaman}")
        return suanki_zaman

class Etkilesimler(ABC):
    def __init__(self, ziyaretci,hayvan):
        self.ziyaretci = ziyaretci
        self.hayvan = hayvan

    @abstractmethod
    def davranis_tepki():
        pass

class Kosma(Etkilesimler):
    def __init__(self, ziyaretci, hayvan):
        super().__init__(ziyaretci, hayvan)
    def davranis_tepki(self):
        print(f"{hayvan} koştuğunda {ziyaretci} güldüler.")

class Yemek(Etkilesimler):
    def __init__(self, ziyaretci, hayvan):
        super().__init__(ziyaretci, hayvan)
    def davranis_tepki(self):
        print(f"{hayvan} yemek yediğinde {ziyaretci} şaşırdılar.")

class Uyuma(Etkilesimler):
    def __init__(self, ziyaretci, hayvan):
        super().__init__(ziyaretci, hayvan)
    def davranis_tepki(self):
        print(f"{hayvan} uyuduğunda {ziyaretci} sessizce izlediler.")


while True:
    h1 = HayvanatBahcesi("Hitit Hayvanat Bahçesi",2020, "Çorum",20)
    print("{0}'ne hoş geldiniz. Yıl:{1} Konum: {2}".format(h1.hayvanat_bahcesi_adi,h1.acilis_yili,h1.bulundugu_sehir))
    print("Müşteri Giriş: 1, Hayvanları Göster: 2, Gözlem Yap: 3, Personel Bilgileri: 4")
    secim = int(input("Lutfen secim yapiniz. : "))

    hayvansozlugu = {1:"aslan",2:"yılan",3:"fil",4:"penguen",5:"papagan",6:"maymun",7:"leopar",8:"zebra",9:"kutupayısı"}
    z1 = Ziyaretci("Ali","Aydın","1","123456",20,"Ailesi","Maymun","ali123")
    p1 = Personeller("Melisa","Çık","melisa123","123456","20.000","veteriner")
    musteri_listesi = []
    personel_listesi = []
    musteri_listesi.append(z1)
    personel_listesi.append(p1)
    if secim == 1 :
        while True:
            print("Müşteri Giriş: 1, Müşteri Kayıt: 2, Müsterileri Listele: 3")
            secim2 = int(input("Lutfen secim yapiniz. : "))
            if(secim2 == 1):
                kullanıcıadi = str(input("Kullanıcı Adı:"))
                şifre = str(input("Şifre:"))
                for i in musteri_listesi:
                    if(str(i.getsifre()) == şifre and str(i.getkullanıcıadi()) == kullanıcıadi):
                        print("Giriş Yapıldı")
                        i.hayvanlari_izle()
                        i.etkilesimde_bulun()
            elif(secim2 == 2):
                k_İsim = input("İsminiz :")
                k_Soyisim = input("Soyisim :")
                k_Tc = input("Tc :")
                k_kullanıcıadi = input("kullanıcıadi :")
                k_Sifre = input("Sifre :")
                k_Yas = input("Yas :")
                grupsecim = int(input("Grup Seçiniz: 1(Aile), 2(Bireysel), 3(Okul) :"))
                if(grupsecim == 1):
                    k_Grup = "Ailesi"
                elif(grupsecim == 2):
                    k_Grup = "Bireyi"
                elif(grupsecim == 3):
                    k_Grup = "Öğrencisi"
                print("Hangi ortamdan hayvan ziyareti yapacaksınız ? (1:Savana) (2:Kutup Bölgesi) (3:Tropikal Orman)")
                ortamsecim = int(input("Seçim yapınız:"))
                if(ortamsecim == 1):
                    savana = Savana()
                    print("Savana Bölgesindeki Hayvanlar Aşağıda Verilmiştir, Hangisini Seçmek İstiyorsunuz ?")
                    for i in range(len(savana.gethayvanlar())):
                        print(f"{i+1}. {savana.gethayvanlar()[i]}")
                    savanasecim = int(input("Seçim Yapınız :"))
                    if(savanasecim == 1):
                        k_İzlenenhayvan = "Aslan"
                    elif(savanasecim == 2):
                        k_İzlenenhayvan = "Zebra"
                    elif(savanasecim == 3):
                        k_İzlenenhayvan = "Fil"
                    elif(savanasecim == 4):
                        k_İzlenenhayvan = "Leopar"
                elif(ortamsecim == 2):
                    kutup = KutupBolgesi()
                    print("Kutup Bölgesindeki Hayvanlar Aşağıda Verilmiştir, Hangisini Seçmek İstiyorsunuz ?")
                    for i in range(len(kutup.gethayvanlar())):
                        print(f"{i+1}. {kutup.gethayvanlar()[i]}")
                    kutupsecim = int(input("Seçim Yapınız :"))
                    if(kutupsecim == 1):
                        k_İzlenenhayvan = "Kutup Ayısı"
                    elif(kutupsecim == 2):
                        k_İzlenenhayvan = "Penguen"
                elif(ortamsecim == 3):
                    tropikalorman = TropikalOrman()
                    print("Tropikal Orman Bölgesindeki Hayvanlar Aşağıda Verilmiştir, Hangisini Seçmek İstiyorsunuz ?")
                    for i in range(len(tropikalorman.gethayvanlar())):
                        print(f"{i+1}. {tropikalorman.gethayvanlar()[i]}")
                    tropikalsecim = int(input("Seçim Yapınız :"))
                    if(tropikalsecim == 1):
                        k_İzlenenhayvan = "Maymun"
                    elif(tropikalsecim == 2):
                        k_İzlenenhayvan = "Papağan"
                    elif(tropikalsecim == 3):
                        k_İzlenenhayvan = "Yılan"
                n1 = Ziyaretci(k_İsim,k_Soyisim,k_Tc,k_Sifre,k_Yas,k_Grup,k_İzlenenhayvan,k_kullanıcıadi)
                musteri_listesi.append(n1)
            elif(secim2 == 3):
                for i in musteri_listesi:
                    print(i.getkullanıcıadi())
    elif secim == 2:
        aslan = Aslan(
           "Kedigil",
           "12",
           "Asya Aslanı",
           "dişi : 160-184 cm , erkek : 184-208 cm",
           "dişi : 150 kilogram , erkek : 255 kilogram"
        )
        yılan = Yılan(
            "Pullular takımına ait uzun,ayaksız etçil sürüngenler.",
            "11",
            "Karayılan(Dolichophis jugularis)",
            "Küçük memeliler kuşlar,kertenkeleler ve yarasalarla beslenir.Ağızlarını kafalarını dört katına kadar açabilirler."
        )
        fil = Fil(
            "Hortumlular(Proboscidea)",
            "70",
            "Asya Fili",
        )
        penguen = Penguen(
            "Spheniscidae familyasında yer alan uçamayan ,yüzemeyen perde ayaklı deniz kuşlarıdır.",
            "10",
            "Kral Penguen",
            "Uzun ince gaga ve boyun ile kulak kısımlarındaki dikkat çekici turuncu renk."
        )
        papagan = Papagan(
            "Psittaciformes takımını oluşturan kıvrık gagalı,parlak tüylü,sıcak yerlerde yaşayan kuşlardır.",
            "10",
            "Cennet Papağanı",
            "10-15"
        )
        maymun = Maymun(
            "Primatlar takımındaki memelilerdir.",
            "20",
            "Aslan Kuyruklu Şebek Maymunu",
            "20 - 35 kilogram",
            "Yaklaşık 1 metre"
        )

        leopar = Leopar(
            "Kedigiller familyasının Panthera cinsi",
            "22",
            "Pars",
            "Leoparların birden fazla eşleri olur ve 1 yıl boyunca ürerler."
        )

        zebra = Zebra(
            "Atgiller(Equidae) familyasından",
            "25",
            "Bayağı Zebra",
            "350 kilograma kadar ulaşabilirler",
            "25-30"
        )

        kutupayısı = Kutup_Ayısı(
            "Ayıgiller(Ursidae) familyasından soğuk kuzey kutup bölgesinin karlı shaillerinde ve buzullar üzerinde yaşayan ayı türüdür",
            "27",
            "Grolar",
            "Genel olarak ilkbahar aylarında çifleşmektedirler.Belirli bir çifleri bulunmamaktadır."          
        )

        print("Hayvanlar Aşağıda Verilmiştir. Detay İçin hayvan numarasını giriniz..")

        for i in hayvansozlugu:
            print(f"{i} : {hayvansozlugu[i]}")
        secim3 = int(input("Seçim Yapınız :"))
    
        if(secim3 == 1):
            print(aslan.hareket_et())
            aslan.hayvan_bilgi()
        elif(secim3 == 2):
            print(yılan.yemek())
            yılan.hayvan_bilgi()
        elif(secim3 == 3):
            print(fil.uyumak())
            fil.hayvan_bilgi()
        elif(secim3 == 4):
            print(penguen.hareket_et())
            penguen.hayvan_bilgi()           
        elif(secim3 == 5):
            print(papagan.yemek())
            papagan.hayvan_bilgi()           
        elif(secim3 == 6):
            print(maymun.yemek())
            maymun.hayvan_bilgi()
        elif(secim3 == 7):
            print(leopar.hareket_et())
            leopar.hayvan_bilgi()  
        elif(secim3 == 8):
            print(zebra.hareket_et())
            zebra.hayvan_bilgi()
        elif(secim3 == 9):
            print(kutupayısı.uyumak())
            kutupayısı.hayvan_bilgi()

    elif secim == 3:
        zaman = ZamanYonetimi()
        simdiki_zaman = zaman.zaman_gecir()
        if(simdiki_zaman == "Gece"):
            print("Bütün Hayvanlar Uyuyor.")
        elif(simdiki_zaman == "Sabah" or simdiki_zaman == "Akşam"):
            print("Bütün Hayvanlar Yemek Yiyor.")
        elif(simdiki_zaman == "Öğle"):
            ziyaretci = random.choice(musteri_listesi)
            ziyaretci = ziyaretci.getgrup()
            hayvan = random.choice(hayvansozlugu)
            etkilesimlistesi = [Kosma, Yemek, Uyuma]
            etkilesim = random.choice(etkilesimlistesi)
            durum = etkilesim(ziyaretci,hayvan)
            durum.davranis_tepki()
    
    elif secim == 4:
        while True:
            print("Personel Giriş: 1, Personel Kayıt: 2, Personel Listele: 3")
            secim2 = int(input("Lutfen secim yapiniz. : "))
            if(secim2 == 1):
                kullanıcıadi = str(input("Kullanıcı Adı:"))
                şifre = str(input("Şifre:"))
                for i in personel_listesi:
                    if(str(i.getpersonelsifre()) == şifre and str(i.getpersonelkullanıcıadi()) == kullanıcıadi):
                        print("Giriş Yapıldı")
                        i.personelbilgi()
                        i.gorevyap()
            elif(secim2 == 2):
                p_İsim = input("İsminiz :")
                p_Soyisim = input("Soyisim :")
                p_kullanıcıadi = input("kullanıcıadi :")
                p_Sifre = input("Sifre :")
                p_Maas = input("Maas :")
                p_Departman = input("Departman :")
                p2 = Personeller(p_İsim,p_Soyisim,p_kullanıcıadi,p_Sifre,p_Maas,p_Departman)
                personel_listesi.append(p2)
            elif(secim2 == 3):
                for i in personel_listesi:
                    print(i.getpersonelkullanıcıadi())
    else:
        print("YANLIŞ TUŞLAMA YAPTINIZ LÜTFEN TEKRAR GİRİŞ YAPINIZ!!!!!!!!!!!!!!!!!!")

