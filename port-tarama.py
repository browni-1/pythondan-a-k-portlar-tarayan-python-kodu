import socket
import sys
from datetime import datetime

def tarama_baslat():
    # Kullanıcıdan hedef bilgisi alınıyor
    hedef = input("Taramak istediğiniz IP adresini veya Domain adını girin: ")

    try:
        # Eğer domain girildiyse IP'ye çevirir
        hedef_ip = socket.gethostbyname(hedef)
    except socket.gaierror:
        print("\n[!] Hata: Host çözülemedi. Lütfen geçerli bir adres girin.")
        sys.exit()

    print("-" * 50)
    print(f"Hedef: {hedef} ({hedef_ip})")
    print(f"Tarama Başlangıcı: {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 50)

    # Taranacak en kritik portlar listesi
    portlar = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]

    try:
        for port in portlar:
            # TCP bağlantı soketi oluşturuluyor
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 1 saniye içinde cevap gelmezse diğer porta geçer
            socket.setdefaulttimeout(1)
            
            # Bağlantıyı dener (0 sonucu başarılı demektir)
            sonuc = s.connect_ex((hedef_ip, port))
            
            if sonuc == 0:
                # Servis adını öğrenmeye çalış (opsiyonel)
                try:
                    servis = socket.getservbyport(port)
                except:
                    servis = "Bilinmiyor"
                print(f"[+] Port {port} Açık \t({servis})")
            
            s.close()

    except KeyboardInterrupt:
        print("\n[!] Tarama kullanıcı tarafından durduruldu.")
        sys.exit()
    except socket.error:
        print("\n[!] Sunucuya bağlanılamadı.")
        sys.exit()

    print("-" * 50)
    print("Tarama tamamlandı.")

if _name_ == "_main_":
    tarama_baslat()
