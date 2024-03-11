def indirim_hesapla(sezon, eski_sayac, yeni_sayac):
    # Sezonlara göre indirim oranlarını belirle
    indirim_oranlari = {
        1: 0.1,  # İlkbahar
        2: 0.15, # Yaz
        3: 0.2,  # Sonbahar
        4: 0.25  # Kış
    }

    # İndirim oranını sezon değerine göre al
    indirim_orani = indirim_oranlari.get(sezon, None)

    # Eğer sezon değeri geçerli değilse hata mesajı ver
    if indirim_orani is None:
        print("Yanlış giriş yaptınız.")
        return None

    # Fatura miktarını hesapla
    fatura_miktari = (yeni_sayac - eski_sayac) * 2.5

    # İndirimi hesapla
    indirim_miktari = fatura_miktari * indirim_orani

    # İndirim sonrası faturayı hesapla
    indirimli_fatura = fatura_miktari - indirim_miktari

    return indirimli_fatura

def main():
    print("Sezona göre faturanın indirim farklarını hesaplayan ve gösteren program...")
    
    while True:
        try:
            sezon = int(input("Lütfen bir sezon giriniz (1: İlkbahar, 2: Yaz, 3: Sonbahar, 4: Kış): "))
            if sezon < 1 or sezon > 4:
                raise ValueError
            eski_sayac = int(input("Eski sayaç değerini giriniz: "))
            yeni_sayac = int(input("Yeni sayaç değerini giriniz: "))

            indirimli_fatura = indirim_hesapla(sezon, eski_sayac, yeni_sayac)
            if indirimli_fatura is not None:
                if sezon == 4:
                    print("Kış Sezonu")
                else:
                    print("Diğer Sezonlar")
                print(f"Faturanız: {indirimli_fatura}")
            break
        except ValueError:
            print("Geçersiz giriş yaptınız. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
