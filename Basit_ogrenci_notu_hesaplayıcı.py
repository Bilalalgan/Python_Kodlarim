class Ogrenci : 
    def __init__(self, isim, vize1, vize2, final, ortalama, harfnotu, ) -> None:
        self.isim = isim
        self.vize1 =vize1
        self.vize2 = vize2
        self.final = final
        self.ortalama =ortalama
        self.harfnotu =harfnotu

    def ogrenci_isimlerini_gir(self):
        global ogrenci_sayısı
        ogrenci_sayısı = int(input("Lütfen öğrenci sayısını giriniz : ")) 
        for i in range(ogrenci_sayısı):
            x = input("Lütfen ögrenci ismini giriniz :")

    def ogrenci_notlari_gir(self):
            self.vize1 = input("Lütfen vize 1 giriniz :") 
            self.vize2 = input("Lütfen vize 2 giriniz :") 
            self.final = input("Lütfen final giriniz :") 

    def ortalama_hesapla_ve_yazdır(self):
            self.ortalama = print((self.vize1*25+self.vize2*35+self.final*40)/100) 

    def harf_notu_yazdır(self):
            if (self.ortalama > 50):
                self.harfnotu = "Geçtiniz.."
            else :
                self.harfnotu = "Kaldınız.."   

    def ogrenci_notları_yazdır(self):
        print("İsim: "+ self.isim + "Vize1:" + self.vize1 + "Vize2:"+ self.vize2 + "Final:" + self.final + "Ortalama:"+ self.ortalama + "Harf:"+self.ortalama)             

ogrenci_notları_dizi = []
Ogrenci.ogrenci_isimlerini_gir(ogrenci_notları_dizi)
Ogrenci.ogrenci_notlari_gir(ogrenci_notları_dizi,"Vize1")
Ogrenci.ogrenci_notlari_gir(ogrenci_notları_dizi,"Vize2")              
Ogrenci.ogrenci_notlari_gir(ogrenci_notları_dizi,"final")
Ogrenci.ortalama_hesapla_ve_yazdır(ogrenci_notları_dizi)
Ogrenci.harf_notu_yazdır(ogrenci_notları_dizi)
Ogrenci.ogrenci_notları_yazdır()

