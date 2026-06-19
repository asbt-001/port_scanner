import socket
from datetime import datetime


print(f" (: time : {datetime.now()}")
ip = input("[+] ip or domain name target :")
port_statr = int(input("[+] port start > 20 :"))
port_fnish = int(input("[+] fnish port < 100 :"))

if port_statr < 20 :
    print("[!] no port start >= 20")
    exit()
    
elif port_fnish > 100:
    print("[!] no port fnish <= 100")
    exit()
    
for port_sc in range(port_statr, port_fnish):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect_ex((ip, port_sc))
    if connect == 0 :
        print(f"[+] port {port_sc} is open")
        
        
# date = 6/19/2026 14:12 PM
