import numbers
import random
import time
import os
import pynput as pp

def num_trick():
    intro = input("This is a Number Trick.\nAre You Ready? (Y or N)\n(Press Enter to continue)\n(Press ESC to close)")
    if intro == None:
        print("Exiting...")
    elif intro == 'y' or 'Y':
        print("I am going to ask you to pick a number")
        time.sleep(3)
        user_num = int(input("Enter a number between 1 and 13: "))
        time.sleep(2)
        print("Now add 4 to your number.")
        time.sleep(2)
        print("Then Multiply that by 2")
        time.sleep(5)
        print("Subtract 6 from that ")
        time.sleep(3)
        print("Divide the Result by 2")
        time.sleep(3)
        print("Finally subtract by your original number:", "(" + str(user_num) +")")
        time.sleep(5)
        print("Remember the number you end up with!")
        time.sleep(1)
        print("I will see if I can guess it!")
        time.sleep(3)
        trick = (((user_num + 4) * 2 - 6) /2) - user_num
        print("Your number was:", format(trick, '.0f'), )
        correct = input("Was I Right?\nY= Yes\nN= No")
        if correct == 'n' or 'N':
            print("Oh, no. What went wrong?")
        elif correct == 'y' or 'Y':
            print("Thanks for playing!")
    else:
        print("Goodbye!")
        exit()
    
    
num_trick()