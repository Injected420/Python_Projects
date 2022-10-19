import time


def add(x, y):
    return format(x + y, ',.3f')


def subtract(x, y):
    return format(x - y, ',.3f')


def multiply(x, y):
    return format(x * y, ',.3f')


def divide(x, y):
    return format(x / y, ',.3f')


def calc_it():
    a = 0
    while a == 0:
        print("Select which to perform")
        time.sleep(1)
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\nQ. Quit")
        time.sleep(1)
        choice = input("[*] Your choice (1,2,3,4) or Q to Quit: ")
        if choice.lower() == "q":
            print("[*] Goodbye!")
            a = 1
        elif choice == "1":
            num1 = float(input("[*] Enter the first number to Add: "))
            num2 = float(input("[*] Enter the second number to Add: "))
            time.sleep(1)
            print(f'[+] {num1} + {num2} equals ' + str(add(num1, num2)))
        elif choice == "2":
            num1 = float(input("[*] Enter the first number to Subtract: "))
            num2 = float(input("[*] Enter the second number to Subtract: "))
            time.sleep(1)
            print(f'[+] {num1} - {num2} equals ' + str(subtract(num1, num2)))
        elif choice == "3":
            num1 = float(input("[*] Enter the first number to Multiply: "))
            num2 = float(input("[*] Enter the second number to Multiply: "))
            time.sleep(1)
            print(f'[+] {num1} * {num2} equals ' + str(multiply(num1, num2)))
        elif choice == "4":
            num1 = float(input("[*] Enter the first number to Divide: "))
            num2 = float(input("[*] Enter the second number to Divide: "))
            time.sleep(1)
            print(f'[+] {num1} / {num2} equals ' + str(divide(num1, num2)))
        else:
            print("[-] Incorrect Entry. Please try again.")


calc_it()
