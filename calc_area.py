import time
import sys


# This program will calculate the area of a cube

def cube_area():
    face = float(input("[*] Enter the size of one side of the cube: "))
    surface_area = face * face * 6
    print("[*] The surface of the cube is: " + format(surface_area, '.3f'))


# cube_area()


def triangle():
    # Greeting
    print("Hi, I can calculate the Area and Perimeter of a Rectangle!")
    time.sleep(2)
    # Start
    print("Ok, let's do this!")
    height = int(input("What is the height: "))
    width = int(input("What is the width: "))
    area = height * width
    perim = 2 * (height + width)
    print("The area of your rectangle is:", area)
    print("The perimeter is:", perim)


# triangle()


def canvote():
    user_age = int(input("[*] Please enter your age: "))
    if user_age < 18:
        print("[*] Sorry you are too young to vote. You need to be 18.")
        time.sleep(1)
        years_until = 18 - user_age
        print("[*] We will check how many years left until you can vote.")
        print("[*] You have " + str(years_until) + " years to go until you can vote.")
    elif user_age >= 18:
        registered = str(input("[*] Have you registered to vote yet?"))
        if registered.lower() == "yes" or registered.lower() == "yea" or registered.lower() == "yup" or registered.lower() == 'y' or registered.lower() == 'Y':
            print("[*] You are able to vote!!")

        elif registered.lower() == "no" or registered.lower() == "na" or registered.lower() == "nope" or registered.lower() == "n" or registered.lower() == "N" or registered.lower() == "Nope":
            print("[*] Sorry you need to register before you can vote.")
        else:
            print("[*] Sorry, incorrect input")


canvote()
