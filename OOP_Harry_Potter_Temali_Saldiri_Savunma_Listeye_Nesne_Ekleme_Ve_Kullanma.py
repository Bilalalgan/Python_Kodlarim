class Obje:
    def __init__(self,isim,obje_dizin):
        
        self.isim = isim
        self.obje_dizin = obje_dizin
    

    def obje_bilgisi_yazdir(self):
        
        print("Karakterin Ismi : ",self.isim)
        

class Karakter(Obje):
    
    def __init__(self,isim ,obje_dizin, Can_Degeri, Hareket_Miktari, techizat_listesi = []):
        
        super().__init__(isim,obje_dizin)
        self.Can_Degeri = Can_Degeri
        self.Hareket_Miktari = Hareket_Miktari
        self.techizat_listesi = techizat_listesi
        
        

    def techizat_ekle(self,Eklenecek_Techizat):
        
        self.techizat_listesi.append(Eklenecek_Techizat)
        
        
        print("Techizat Listesi")
        print("****************\n")
        for i in self.techizat_listesi:
            print("{}  {}  {}  {}".format(i.isim,i.obje_dizin,i.Techizat_Hasar_Miktari,i.Techizat_Savunma_Miktari))
        
        print("\n\n\"Techizat Eklendi\"\n\n")
    
    
    def obje_bilgisi_yazdir(self):
        
    
        print("{0} Isimli, yeri : {1}, Can Degeri : {2}, Hareket Miktari : {3}".format(self.isim, self.obje_dizin, self.Can_Degeri, self.Hareket_Miktari))
    
    
    
    
    def saldiri_yap(self, List_Yeri, Kisi):
        
        print("\nSaldiridan Onceki Can Degeri",Kisi.Can_Degeri)
        
        Guncel_Can = Kisi.Can_Degeri - self.techizat_listesi[List_Yeri].Techizat_Hasar_Miktari
        
        print("Guncel Can : ",Guncel_Can)


class Techizat(Obje):
    
    def __init__(self,isim ,obje_dizin, Techizat_Hasar_Miktari, Techizat_Savunma_Miktari):
        
        super().__init__(isim ,obje_dizin)
        self.Techizat_Hasar_Miktari = Techizat_Hasar_Miktari
        self.Techizat_Savunma_Miktari = Techizat_Savunma_Miktari
        
        
    def techizat_guclendir(self, Hasar, Savunma):
        
        print("Techizat Saldiri Eski Degeri : ", self.Techizat_Hasar_Miktari)
        print("Techizat Saldiri Guclendirilmis Degeri : ", self.Techizat_Hasar_Miktari+Hasar)
        print("Techizat Savunma Eski Degeri : ", self.Techizat_Savunma_Miktari)
        print("Techizat Savunma Guclendirilmis Degeri : ", self.Techizat_Savunma_Miktari+Savunma)
    
    
    def techizat_yazdir(self):
        
        print("\n{0}, {1}, {2}, {3}".format(self.isim, self.obje_dizin, self.Techizat_Hasar_Miktari, self.Techizat_Savunma_Miktari))



print("************************************************")
obje = Obje("Marcus","Karakter Resimleri/Kisi/Marcus.jpg")
obje.obje_bilgisi_yazdir()


    

karakter1 = Karakter("Harry Potter","Karakter resimleri/Kisi/Harry Potter.jpg",100.0,2)
techizat1 = Techizat("Kilic","techizat resimleri/kilic.jpg",5.0,0.0)
techizat2 = Techizat("Kalkan","techizat resimleri/kalkan.jpg",1.0,10.0)


karakter1.techizat_ekle(techizat1)

karakter1.techizat_ekle(techizat2)
    

karakter2 = Karakter("Voldemort","karakter resimleri/kisi/voldemort.jpg",250,5,[Techizat("Asa","techizat resimleri/kilic.jpg",7,5)])



karakter1.obje_bilgisi_yazdir()
karakter2.obje_bilgisi_yazdir()



karakter1.saldiri_yap(0,karakter2)

karakter2.saldiri_yap(0,karakter1)

karakter1.saldiri_yap(0,karakter2)



karakter_techizat = karakter1.techizat_listesi[0]

karakter_techizat.techizat_guclendir(10,5)

karakter1.techizat_listesi[0].techizat_yazdir()
    
