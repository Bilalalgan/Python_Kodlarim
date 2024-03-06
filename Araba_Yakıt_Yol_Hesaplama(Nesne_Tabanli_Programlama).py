class Car:
    
    def __init__(self , Isim , Model):
        
        self.Isim = Isim
        self.Model = Model
        self.Yakit = 0
        self.Yol = 0
        self.Km_Basina_Yakma = 0.02
        self.gidebilecek = 0
        self.Girdi = 1
    
    def araba(self):
        self.Isim = input("arabanin Markasini Giriniz : ")
        self.Model = input("\narabanin Modelini Giriniz : ")
        
        print("{0} markali, {1} model olan araba ".format(self.Isim,self.Model))
        
    def Benzin_Durumu(self):
        
        print("\nBenzin Durumu : ",self.Yakit)
        
        
    
    def Kalan_Yakit_Hesapla(self, Km):
        

        self.Yakit = self.Yakit - (Km * self.Km_Basina_Yakma)
        
        self.gidebilecek = self.Yakit / self.Km_Basina_Yakma
        
        if self.Yakit <=0:
            
            
            print("Yakitiniz Gideceginiz Yere Kadar Yetmedi, Max Gidilebilecek Km : ",self.gidebilecek)
            
        else:
            
        
            print("\n{0} Km Gidebilirsiniz".format(self.gidebilecek))
            
            
        self.gidebilecek += self.gidebilecek
        global Girdi
        Girdi = 1
        
        
        
        
    
    def Benzin_Doldur(self, Yakit_Miktari):
        
        
        self.Yakit = self.Yakit + Yakit_Miktari
        print("\nGuncel Yakit Miktari : ",self.Yakit)
        
    
    
    def Gidilen_Yol_Miktari_Yazdir(self):
        
        print("Gidilen Toplam Yol Miktari : ",self.gidebilecek)
        
        
        
        
    
    
Nesne = Car("Isim","Model")



Nesne.araba()
Nesne.Benzin_Durumu()

Yakit_Miktari = int(input("Kaç Litre Yakit Eklemek Istersiniz : "))

Nesne.Benzin_Doldur(Yakit_Miktari)

Km = int(input("Kac Km Gideceksiniz : "))

Nesne.Kalan_Yakit_Hesapla(Km)

Girdi = int(input("Basa Donmek Icin \"0\" basınız : \n devam etmek icin 1 basınız : "))


# BURADA MAX 2 KERE DONUYO FARKLI BIR OGE KOYMAK LAZIM

if Girdi == 0:

    Nesne.Benzin_Durumu()

    Yakit_Miktari = int(input("Kaç Litre Yakit Eklemek Istersiniz : "))

    Nesne.Benzin_Doldur(Yakit_Miktari)

    Km = int(input("Kac Km Gidiceksiniz : "))

    Nesne.Kalan_Yakit_Hesapla(Km)
    
else:
    
    Nesne.Gidilen_Yol_Miktari_Yazdir()