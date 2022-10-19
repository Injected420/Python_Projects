def ascii_value():
    c = input("[*] Enter a character from the keyboard: ")
    print("[*] The ASCII value of", c, "is", ord(c))


if __name__ == "__main__":
    print("[*] ASCII Value of any keyboard character ")
    cont = input(
        "[*] To continue enter [y]\n[*] To Quit enter [q]\n[*] Enter: ")
    if cont == "y" or "Y":
        ascii_value()
        cont = input(
            "[*] To continue enter [y]\n[*] To Quit enter [q]\n[*] Enter: ")
    elif cont == "q" or "Q":
        print("[*] Goodbye!")
