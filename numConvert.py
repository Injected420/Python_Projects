def hex_to_decimal(hex_string: str) -> int:
    hex_table = {hex(i)[2:]: i for i in range(16)}
    hex_string = hex_string.strip().lower()
    if not hex_string:
        raise ValueError("An empty string was passed to the function.")
    is_negative = hex_string[0] == "-"
    if is_negative:
        hex_string = hex_string[1:]
    if not all(char in hex_table for char in hex_string):
        raise ValueError("A Non-hexadecimal value was passed to the function.")
    decimal_number = 0
    for char in hex_string:
        decimal_number = 16 * decimal_number + hex_table[char]
    return -decimal_number if is_negative else decimal_number


def bin_to_decimal(bin_string: str) -> int:
    bin_string = str(bin_string).strip()
    if not bin_string:
        raise ValueError("Empty string was passed to the function.")
    is_negative = bin_string[0] == "-"
    if is_negative:
        bin_string = bin_string[1:]
    if not all(char in "01" for char in bin_string):
        raise ValueError("Non-binary value was passed to the function.")
    decimal_number = 0
    for char in bin_string:
        decimal_number = 2 * decimal_number + int(char)
    return -decimal_number if is_negative else decimal_number


def convert_to_fahrenheit():
    tempC = float(input("Enter the temperature in Celius to be converted Farenheit: "))
    temp_in_f = tempC * 1.8 + 32
    print("[+]", tempC, "Celius is", temp_in_f, "in Fahrenheit.")
    return temp_in_f


def convert_to_celius():
    tempF = float(input("Enter the temperature in Farenheit to be converted to Celius: "))
    temp_in_c = (tempF - 32) / 1.8
    print("[+]", tempF, "Farenheit equals", temp_in_c, "celius.")
    return temp_in_c


def celius_to_kelvin():
    tempC = float(input("Enter the temperature in Celius to be converted to Kelvin: "))
    kelvin = tempC + 273.15
    print("[+]", tempC, "celius equals", kelvin, "kelvin.")
    return kelvin


def main():
    a = 0
    while a == 0:
        print("Welcome user!")
        choice = input(
            "Enter 'C' to convert Celius to Farenheit.\n\rEnter 'F' to convert Farenheit to Celius\n\rEnter 'K' to convert Celius to Kelvin. ")
        if choice == 'C' or 'c':
            convert_to_fahrenheit()
        elif choice == 'F' or 'f':
            convert_to_celius()
        elif choice == 'K' or 'k':
            celius_to_kelvin()
        else:
            print(ValueError, 'Incorrect Entry')
