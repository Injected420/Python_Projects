import requests
import time


def ask_names():
    print(f'[*]Hello!')
    ask_name = input(f'[*]What is your name?\r\n')
    print("[*]Hi", ask_name, "it is very nice to meet you.")
    siblings = input("[*]" + ask_name +
                     ", do you have any brothers or sisters?\n")
    if siblings == "yes" or siblings == "y" or siblings == "Yea" or siblings == "Yes":
        print("[*]That's so cool!")
        s_num = int(input("[*]How many?\r\n"))
        print(str(s_num) + "! Wow, that's a lot!")
        while s_num > 0:
            s_num -= 1
            sib_names = input("Name 1: \r\n")
            sib_list = []
            sib_list +=             
        print(sib_list)
    elif siblings == "No" or siblings == "n" or siblings == "no" or siblings == "N":
        print("[*]Really?!\r\nI am an only child too!")
    else:
        print("Please use only yes/yea or no.")

ask_names()
