uzaklık_listesi = []
noktalar = []

def orjine_uzaklık(liste):
    for i in range(len(liste)):
        x = int(liste[i][0])
        y = int(liste[i][1])
        z = int(liste[i][2])
        uzaklık = ((x)**2) + ((y)**2) + ((z)**2)
        uzaklık = (uzaklık)**1/2
        uzaklık_listesi.append(uzaklık)
    return(uzaklık_listesi)

def sırala(liste):
    en_buyuk = liste[0]
    for i in range(1, len(liste)):
        if liste[i] > en_buyuk:
            en_buyuk = liste[i]
    return liste.index(en_buyuk)

for i in range(5):
    x = input("{0}.noktanın X degerini giriniz :  ".format(i))
    y = input("{0}.noktanın Y degerini giriniz :  ".format(i))
    z = input("{0}.noktanın Z degerini giriniz :  ".format(i))
    noktalar.append((x,y,z))

print("Orjine en uzak nokta {}. Noktadır".format(sırala(orjine_uzaklık(noktalar))))
