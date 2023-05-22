import random

def kart_ver():
    kartlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return random.choice(kartlar)

def skor_hesapla(kartlar):
    if sum(kartlar) == 21 and len(kartlar) == 2:
        return 0  # Blackjack
    if 11 in kartlar and sum(kartlar) > 21:
        kartlar.remove(11)
        kartlar.append(1)
    return sum(kartlar)

def sonucu_karsilastir(oyuncu_skoru, bilgisayar_skoru):
    """Skorları karşılaştırarak sonucu belirler."""
    if oyuncu_skoru == bilgisayar_skoru:
        return "Berabere!"
    elif bilgisayar_skoru == 0:
        return "Bilgisayar blackjack yaptı. Kaybettiniz!"
    elif oyuncu_skoru == 0:
        return "Blackjack yaptınız! Kazandınız!"
    elif oyuncu_skoru > 21:
        return "El skoru 21'i geçti. Kaybettiniz!"
    elif bilgisayar_skoru > 21:
        return "Bilgisayar el skoru 21'i geçti. Kazandınız!"
    elif oyuncu_skoru > bilgisayar_skoru:
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

print("\n\n************* Blackjack Oyunumuza Hoş Geldiniz. **********")

oyuncu_kartlari = []
bilgisayar_kartlari = []
oyun_sonu = False

for i in range(2):
    oyuncu_kartlari.append(kart_ver())
    bilgisayar_kartlari.append(kart_ver())

while not oyun_sonu:
    oyuncu_skoru = skor_hesapla(oyuncu_kartlari)
    bilgisayar_skoru = skor_hesapla(bilgisayar_kartlari)

    print(f"\nEl kartlarınız: {oyuncu_kartlari}, mevcut skorunuz: {oyuncu_skoru}\n")
    print(f"Bilgisayarın ilk kartı: {bilgisayar_kartlari[0]}\n")

    if oyuncu_skoru == 0 or bilgisayar_skoru == 0 or oyuncu_skoru > 21:
        oyun_sonu = True
    else:
        devam_etmek = input("Kart almak için 'e' tuşuna basın, pas geçmek için 'h' tuşuna basın: ")
        if devam_etmek == 'e':
            oyuncu_kartlari.append(kart_ver())
        else:
            oyun_sonu = True

while bilgisayar_skoru != 0 and bilgisayar_skoru < 17:
    bilgisayar_kartlari.append(kart_ver())
    bilgisayar_skoru = skor_hesapla(bilgisayar_kartlari)

print(f"\nEl kartlarınız: {oyuncu_kartlari}, skorunuz: {oyuncu_skoru}")
print(f"Bilgisayarın kartları: {bilgisayar_kartlari}, skoru: {bilgisayar_skoru}")

oyun_sonucu = sonucu_karsilastir(oyuncu_skoru, bilgisayar_skoru)
print(oyun_sonucu)