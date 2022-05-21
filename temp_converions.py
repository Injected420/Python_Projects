def convert_to_fahrenheit():
    tempC = float(input("Enter the temperature in Celius to be converted Farenheit: "))
    temp_in_f = tempC * 1.8 + 32
    print("[+]", tempC,"Celius is", temp_in_f,"in Fahrenheit.")
    return temp_in_f


def convert_to_celius():
    tempF = float(input("Enter the temperature in Farenheit to be converted to Celius: "))
    temp_in_c = (tempF -32) / 1.8
    print("[+]", tempF,"Farenheit equals", temp_in_c,"celius.")
    return temp_in_c

def celius_to_kelvin():
    tempC = float(input("Enter the temperature in Celius to be converted to Kelvin: "))
    kelvin = tempC + 273.15
    print("[+]",tempC,"celius equals",kelvin,"kelvin.")
    return kelvin

def main():
    a = 0
    while a == 0:
        print("Welcome user!")
        choice = input("Enter 'C' to convert Celius to Farenheit.\n\rEnter 'F' to convert Farenheit to Celius\n\rEnter 'K' to convert Celius to Kelvin. ")
        if choice == 'C' or 'c':
            convert_to_fahrenheit()
        elif choice == 'F' or 'f':
            convert_to_celius()
        elif choice == 'K' or 'k':
            celius_to_kelvin()
        else:
            print(ValueError, 'Incorrect Entry')

main()
