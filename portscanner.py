#!/usr/bin/python3
import socket
import sys
from time import sleep
from os import system

system('cls||clear')

print("""
    
    _    _    _____ _  _  ____                       _ _         
   / \  | | _|___  | || |/ ___|  ___  ___ _   _ _ __(_) |_ _   _ 
  / _ \ | |/ /  / /| || |\___ \ / _ \/ __| | | | '__| | __| | | |
 / ___ \|   <  / / |__   _|__) |  __/ (__| |_| | |  | | |_| |_| |
/_/   \_\_|\_\/_/     |_||____/ \___|\___|\__,_|_|  |_|\__|\__, |
                                                           |___/ 


""")

sleep(1)

print("By SonTürk Ak")

sleep(2)

def scanHost(ip, startPort, endPort):
    """ Belirli bir IP adresinde TCP tonu başlatır """

    print('[*] Tarama başlatıldı! %s' % ip)

    # Ana bilgisayarda TCP tonu başlat
    tcp_scan(ip, startPort, endPort)

    print('[+] İşlem %s Tamamlandı' % ip)


def scanRange(network, startPort, endPort):
    """ Belirli bir IP adresi aralığında TCP tonu başlatır """

    print('[*] TCP bağlantısı taramaya başlandı. %s.0' % network)

    # Bir dizi ana bilgisayar IP adresi üzerinde titreşin ve her hedefi taz
    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, startPort, endPort)

    print('[+] TCP port taraması %s.0 Tamamlandı' % network)


def tcp_scan(ip, startPort, endPort):
    """ Bir TCP soketi oluşturur ve sağlanan bağlantı noktaları üzerinden bağlanmaya çalışır """

    for port in range(startPort, endPort + 1):
        try:
            # Yeni bir soket oluşturun
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Bağlantı noktası açıksa yazdır
            if not tcp.connect_ex((ip, port)):
                print('[+] %s:%d/TCP Open' % (ip, port))
                tcp.close()
                
        except Exception:
            pass


if __name__ == '__main__':
    # Saniye cinsinden zaman ala
    socket.setdefaulttimeout(0.01)

    if len(sys.argv) < 4:
        print('Kullanım: ./portscanner.py <IP address> <başlangıç port> <bitiş port>')
        print('Örnek: ./portscanner.py 192.168.1.10 1 65535\n')
        print('Kullanım: ./portscanner.py <network> <başlangıç port> <bitiş port> -n')
        print('Örnek: ./portscanner.py 192.168.1 1 65535 -n')

    elif len(sys.argv) >= 4:
        network   = sys.argv[1]
        startPort = int(sys.argv[2])
        endPort   = int(sys.argv[3])

    if len(sys.argv) == 4:
        scanHost(network, startPort, endPort)

    if len(sys.argv) == 5:
        scanRange(network, startPort, endPort)
web = "WebAltay Destekleriyle Beraber"


print("")

print(web)
print("SonTürk Ak Sunar..")
