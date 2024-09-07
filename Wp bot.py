from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

# WebDriver için Chrome'u kullanacağız
driver = webdriver.Chrome()

# WhatsApp Web sayfasına git
driver.get("https://web.whatsapp.com")

# Kullanıcıdan WhatsApp Web'e giriş yapmasını bekliyoruz (QR kodu taraması gerekiyor)
input("Lütfen QR kodu tarayıp giriş yapın ve bir sohbet penceresine gelin. Devam etmek için Enter'a basın...")

# Sohbet penceresindeki mesaj yazma kutusunu bulun
message_box = driver.find_element("xpath", "//div[@contenteditable='true' and @role='textbox']")

# Mesaj yazma, silme ve durum kontrolü işlemlerini tek bir fonksiyona birleştirdik
def send_message_and_check_status():
    try:
        while True:
            # Mesaj gönder
            message_box.send_keys("abc")
            message_box.send_keys(Keys.ENTER)
            time.sleep(7)  # Mesajın gönderilmesi için kısa bir süre bekle

            # Mesajı sil
            message_box.send_keys(Keys.CONTROL + "a")  # Tüm mesajı seç
            message_box.send_keys(Keys.BACKSPACE)  # Mesajı sil
            time.sleep(7)  # Bir sonraki adıma geçmeden önce kısa bir süre bekle

            # Belirtilen XPath'teki yazıyı al
            try:
                status_element = driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/div[4]/div/header/div[2]/div[2]/span")
                status_text = status_element.text.strip()
                if status_text:
                    current_time = datetime.now().strftime("%H:%M:%S")
                    print(f"Durum: {status_text} - Saat: {current_time}\n")
            except:
                pass  # Herhangi bir durumu bulamazsa hiçbir şey yazdırma

            # Bir sonraki döngüye geçmeden önce bekle
            time.sleep(10)

    except KeyboardInterrupt:
        print("İşlem durduruldu.")
        driver.quit()  # Tarayıcıyı kapat

# Fonksiyonu çalıştır
send_message_and_check_status()
