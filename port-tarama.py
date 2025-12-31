import socket

def port_tara(hedef, portlar):
    print(f"\n--- {hedef} taranıyor... ---\n")
    
    for port in portlar:
        # socket nesnesi oluşturuluyor (AF_INET: IPv4, SOCK_STREAM: TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bağlantı denemesi için zaman aşımı süresi (saniye)
        s.settimeout(1)
        
        # connect_ex hata kodu döndürür (0 ise port açıktır)
        sonuc = s.connect_ex((hedef, port))
        
        if sonuc == 0:
            print(f"[+] Port {port}: AÇIK")
        else:
            # İsteğe bağlı: Kapalı portları görmek istemiyorsanız pass geçebilirsiniz
            print(f"[-] Port {port}: Kapalı")
            
        s.close()

# Kullanım:
hedef_ip = "8.8.8.8" # Veya "google.com"
taranacak_portlar = [21, 22, 53, 80, 443, 3306]

port_tara(hedef_ip, taranacak_portlar)