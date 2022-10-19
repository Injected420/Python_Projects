import datetime
import math
import random
import sys
import time
from tokenize import Number
from tracemalloc import start
import doctest
import argparse

AIR_MAX_TEMP = 135
AIR_AVG_TEMP = 90
AIR_LOW_TEMP = 65


def turn_on_airCon() -> int:
    start_temp = float(input("[*]What is the Temperature?\r\n[*] "))
    if start_temp > AIR_AVG_TEMP or start_temp > AIR_MAX_TEMP:
        print("Turning on Air Condintioner")
    elif start_temp <= AIR_AVG_TEMP:
        print("[*]The temperature is:", start_temp)
    elif start_temp < AIR_LOW_TEMP:
        print("[*]Do You Want to turn on the Heater?")
    elif start_temp == AIR_LOW_TEMP:
        print("[*] It's a nice day!")
    elif start_temp is nan:
        print("[*]The input must be a number.")
    else:
        print("WRONG!")
        sys.exit(0)


def change_temp() -> int:

    __annotations__
