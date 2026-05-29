
import re

def anahtar_kelime_kontrolu(metin):
    supheli_kelimeler = ["askıya alındı", "acil", "giriş yapın", "şifre yenile", "giriş yap", "ödül", "kazandınız", "doğrulayın"]
    tespit_edilenler = []
    temiz_metin = metin.lower()
    
    for kelime in supheli_kelimeler:
        if kelime in temiz_metin:
            tespit_edilenler.append(kelime)
            
    return tespit_edilenler

def link_kontrolu(metin):
    link_formulu = r'https?://[^\s]+'
    linkler = re.findall(link_formulu, metin)
    
    supheli_link_sayisi = 0
    for link in linkler:
        if "bit.ly" in link or "tinyurl.com" in link:
            supheli_link_sayisi += 1
            
    return linkler, supheli_link_sayisi

def mail_analiz_et(metin):
    kelimeler = anahtar_kelime_kontrolu(metin)
    linkler, supheli_link_skoru = link_kontrolu(metin)
    
 
    risk_skoru = len(kelimeler) * 1 + supheli_link_skoru * 2
    
    print("\n" + "="*40)
    print("🛡️  SİBER GÜVENLİK E-POSTA ANALİZ RAPORU  🛡️")
    print("="*40)
    print(f"🚨 Tespit Edilen Şüpheli Kelimeler: {kelimeler}")
    print(f"🔗 Bulunan Toplam Link Sayısı: {len(linkler)}")
    print(f"⚠️  Kısaltılmış/Şüpheli Link Sayısı: {supheli_link_skoru}")
    print("-"*40)
    
    print(f"📊 TOPLAM RİSK SKORU: {risk_skoru}")
    if risk_skoru >= 4:
        print("🔴 SONUÇ: BU BİR PHISHING (OLTALAMA) MAİLİDİR! KESİNLİKLE TIKLAMAYIN.")
    elif 1 <= risk_skoru < 4:
        print("🟡 SONUÇ: ŞÜPHELİ AKTİVİTE. DİKKATLİ OLUNMALIDIR.")
    else:
        print("🟢 SONUÇ: TEMİZ. BELİRGİN BİR TEHDİT BULUNAMADI.")
    print("="*40 + "\n")

if __name__ == "__main__":
    test_maili = """
    Kimden: security-alert@paypal-update-service.com
    Konu: HESABINIZ ASKIYA ALINDI!

    Sayın Müşterimiz,
    Hesabınızda şüpheli işlemler tespit edilmiştir. 24 saat içinde bilgilerinizi doğrulamazsanız hesabınız kalıcı olarak kapatılacaktır.

    Lütfen hemen aşağıdaki linke tıklayarak giriş yapın ve şifrenizi yenileyin:
    http://bit.ly/fake-paypal-login-3829

    Teşekkürler,
    PayPal Güvenlik Ekibi
    """
    
    mail_analiz_et(test_maili)