class Personel:
    def __init__(self, Ad, Soyad, Yas, Birim):
        self.Ad = Ad
        self.Soyad = Soyad
        self.Yas = Yas
        self.Birim = Birim
        
    
    def Bilgi_Goster(self):
        
        print("{} , {} , {} , {}".format(self.Ad,self.Soyad,self.Yas,self.Birim))
    
    

class Egitim(Personel):
    
    def __init__(self, Ad, Soyad, Yas, Birim):
        
        super().__init__(Ad,Soyad,Yas,Birim)
        
    def Bilgi_Guncelle(self):
        pass
    
    def Bilgi_Ekle(self):
        pass
    
    def Bilgi_Sil(self):
        pass
    
    def Bilgi_Goster(self):
        
        print("\nChild Class Calisti\n")
        
        print("{} , {} , {} , {}".format(self.Ad,self.Soyad,self.Yas,self.Birim))
    
    
    
o1 = Personel("Bilal","Arslan","20","Bilgisayar Muhendisligi")

o1.Bilgi_Goster()


# ************************************************************


o2 = Personel("Ahmet","Bayrak","18","Eczacilik")

Egitim.Bilgi_Goster(o1)

Egitim.Bilgi_Goster(o2)


# ************************************************************

# Ana Class'a Nesne Tanimladigimiz Gibi, Child Class'lara da Nesne Tanimlayabiliriz.


o3 = Egitim("Halil Ibrahim","Sisman","26","Computer Engineer")

Egitim.Bilgi_Goster(o3)



        
        
        