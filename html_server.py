import requests
import threading
import socket

ADDRESS = input("Enter the address you want to connect to: ")


def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ADDRESS, 6666))
    info = sock.recv(4096)
    print(info)
    sock.close()


create_socket()
