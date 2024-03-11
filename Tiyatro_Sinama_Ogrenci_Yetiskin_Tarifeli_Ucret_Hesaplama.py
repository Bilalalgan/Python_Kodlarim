print("-- MAGAZAMIZA HOSGELDİNİZ --")


Yetiskin_Ucret = 100

Ogrenci_Ucret = 50

Toplam_Para = 0

Girdi_1 = int(input("1-) Tiyatro\n2-) Sinema\n\nSeciminizi yapiniz : "))

if Girdi_1 == 1:
        
   
    Girdi_2 = int(input("1- Ogrenci Tarifesi\n2- Yetiskin Tarifesi\n\nSeciminizi yapiniz : "))
    
    if Girdi_2 == 1:
        
        Ogrenci_Sayisi_1 = int(input("Ogrenci Sayisi Giriniz : "))
        
        Toplam_Para = Ogrenci_Ucret * Ogrenci_Sayisi_1  
        
    
    elif Girdi_2 == 2:
    
        Yetiskin_Sayisi_1 = int(input("Yetiskin Sayisi Giriniz : "))
        
        Toplam_Para = Yetiskin_Ucret * Yetiskin_Sayisi_1
    
    else:
        print("Hatali Bir Ifade Girdiniz...")
    
        
elif Girdi_1 == 2:
       
    Girdi_2 = int(input("1- Ogrenci Tarifesi\n2- Yetiskin Tarifesi\n\nSeciminizi yapiniz : "))

    if Girdi_2 == 1:
        
        Ogrenci_Sayisi_2 = int(input("Ogrenci Sayisi Giriniz : "))
        
        
        Toplam_Para = Ogrenci_Ucret * Ogrenci_Sayisi_2   
    
    elif Girdi_2 == 2:
        
        Yetiskin_Sayisi_2 = int(input("Yetiskin Sayisi Giriniz : "))
        
        Toplam_Para = Yetiskin_Ucret * Yetiskin_Sayisi_2
    
    else:
        print("Hatali Bir Ifade Girdiniz...")
       
else:
    print("Hatali Bir Ifade Girdiniz...")
    
print("Ucretiniz : ", Toplam_Para)


    


