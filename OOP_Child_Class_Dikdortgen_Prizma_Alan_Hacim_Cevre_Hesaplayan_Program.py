class Geometri:

    def __init__(self,kenar_sayisi):
        self.kenar_sayisi = kenar_sayisi
        self.kenarlar = []
        
        
    def kenarlari_gir(self):
        
        print("{0} Adet Kenar Giriniz...".format(self.kenar_sayisi))
        print("-------------------------")
        
        for i in range(self.kenar_sayisi):
            
            Girdi = int(input("{0}. Kenari Giriniz : ".format(i+1)))
            self.kenarlar.append(Girdi)
            
        print("\n***************************")
        
    
    def kenarlari_listele(self):
        
        print()
        for i in range(len(self.kenarlar)):
            print("{0}. Kenarin Uzunlugu : {1}".format(i+1, self.kenarlar[i]))
            
        print("\n------------------")
    



# Child Class
class Dikdortgen_Prizma(Geometri):
    
    def __init__(self,kenar_sayisi):
        
        super().__init__(kenar_sayisi)
        
    
    def hacim_hesapla(self):
        
        Hacim = 1
        
        for j in range(self.kenar_sayisi):
            
            Hacim *= self.kenarlar[j]
             
        print("Hacim : ", Hacim , "br³")
        print("------------------")
    
    
    def alan_hesapla(self):
        
        A = self.kenarlar
        
        Alan = 2 * (((A[0] * A[1]) + (A[1] * A[2]) + (A[0] * A[2])))
        
        print("Alan : ", Alan , "br²")
        print("------------------")
        
    
    def cevre_hesapla(self):
        
        A = self.kenarlar
        
        Cevre = (A[0] + A[1] + A[2]) * 4
        
        print("Cevre : ", Cevre ,"br")
        print("------------------")
    


dik_pri = Dikdortgen_Prizma(3)
dik_pri.kenarlari_gir()
dik_pri.kenarlari_listele()
dik_pri.hacim_hesapla()
dik_pri.alan_hesapla()
dik_pri.cevre_hesapla()


