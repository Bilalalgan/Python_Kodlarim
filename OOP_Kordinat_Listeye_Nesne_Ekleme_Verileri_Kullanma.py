class Obje:
    
    
    def __init__(self,obje,obje_dizin):
        self.obje = obje 
        self.obje_dizin = obje_dizin
        
        
        
    def obje_bilgisi_yazdir(self):
        print(self.obje)
        
        
        
        
    def isim_duzenle(self,yeni_isim):
        self.obje = yeni_isim





class Daire(Obje):
    
    
    def __init__(self,obje,obje_dizin,renk,boyut = {"En" : 50 , "Boy":50,"genislik":40}):
        super().__init__(obje,obje_dizin)
        self.boyut = boyut
        self.Esya_objeler = []
        self.renk = renk
        
        
        
    def bilgi_göster(self):
        print(self.boyut,self.renk,self.obje)
        
        
        
    def boyut_arttir(self,n,m):
        self.n = n
        self.m = m
        self.boyut["En"] =  self.boyut["En"] + n
        self.boyut["Boy"] = self.boyut["Boy"] + m
        
        
        
    def Esya_Ekle(self,v):
        self.Esya_objeler.append(v)
        
        
        
    def Esya_göster(self):
        
        print("renk : ",self.renk)
        
        for i in self.Esya_objeler:
            
            print("{}  Kordinatlar :  {}  {}  {}".format(i.obje,i.obje_dizin,i.x,i.y))
        

    
        

class Esya(Obje):
    
    sayi = 0
    
    
    def __init__(self,obje,obje_dizin,x = 0,y = 0):
        super().__init__(obje,obje_dizin)
        self.x = x
        self.y = y
        Esya.sayi_arttir()
        
        
        
    def kordinat_degistir(self,new_x,new_y):
        self.x = new_x
        self.y = new_y
        
        
    @classmethod
    def sayi_arttir(cls):
        cls.sayi += 1
        
        
    @classmethod
    def sayi_yazdir(cls):
        print("{} Adet Esya Vardir.".format(cls.sayi))
        
    
    

        
g1 = Daire("kalem",3,"kirmizi",{"En":15,"Boy":25,"genislik":40})

g1.boyut_arttir(5, 10)

a1 = Obje("Nesne Tabanli Programlama",5)

a1.obje_bilgisi_yazdir()

g1.bilgi_göster()

t1 = Esya("Kalem",5,10,15)

t2 = Esya("bilgisayar",10,20,30)

t3 = Esya("klavye",15,20,25)


g1.Esya_Ekle(t1)

g1.Esya_Ekle(t2)

g1.Esya_Ekle(t3)

g1.Esya_göster()

Esya.sayi_yazdir()


