# %%
import socket
import threading
import theHarvester
import IPy as ipy
import requests



def checkIP(ip):
    try:
        ipy.IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


def port_scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.10)
        sock.connect((ipaddress, port))
        print('[+] Port ' + str(port) + ' is Open.')

    except:
        print('[-] Port ' + str(port) + ' is Closed')

IPADDRESS = input("$ Enter Target to Scan: ")
port = int(input("$ Enter the last port number you want to scan: "))
port = range(port)

converted_ip = checkIP(IPADDRESS)
def do_scan():
    for i in port:
        port_scan(converted_ip, port[i])

do_scan()
