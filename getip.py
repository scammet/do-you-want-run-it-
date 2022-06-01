import socket
from requests import get
import csv
import smtplib as smtp
from getpass import getpass

# Определяем имя устройства в сети
hostname = socket.gethostname()
# Определяем локальный (внутри сети) IP-адрес
local_ip = socket.gethostbyname(hostname)
# Определяем глобальный (публичный / в интернете) IP-адрес
public_ip = get('http://api.ipify.org').text
ips=[]
class scam():
    def get_ip():
        ips.append({
            'pc_name':(hostname),
            'public_ip':(local_ip),
            'local_ip':(public_ip)
        })
        print(ips)
    get_ip()
#from scam import *
#print(scam.ips)
