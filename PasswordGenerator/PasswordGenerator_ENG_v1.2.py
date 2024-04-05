import random

def generate_simple_password():
    passlen = 0
    while passlen < 20 or passlen > 92:
        try:
            passlen = int(input("Enter the length of password (between 20 and 92): "))
            if passlen < 20 or passlen > 92:
                print("Password length must be between 20 and 92.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&'()*+,-./:;<=>?@[]^_`{|}~"
    p = "".join(random.sample(s, passlen))
    print("Simple password generated: ", p)

def generate_complex_password():
    passlen = 0
    while passlen < 20 or passlen > 92:
        try:
            passlen = int(input("Enter the length of password (between 20 and 92): "))
            if passlen < 20 or passlen > 92:
                print("Password length must be between 20 and 92.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    include_symbols = ''
    include_numbers = ''
    include_uppercase = ''
    
    while include_symbols != 'y' and include_numbers != 'y' and include_uppercase != 'y':
        include_numbers = input("Include numbers? (y/n): ").lower()
        include_uppercase = input("Include uppercase letters? (y/n): ").lower()
        include_symbols = input("Include symbols? (y/n): ").lower()
        
        if include_symbols != 'y' and include_numbers != 'y' and include_uppercase != 'y':
            print("At least one of the requirements must be selected.")
    
    s = "abcdefghijklmnopqrstuvwxyz"
    
    if include_numbers == 'y':
        s += "0123456789"
    if include_uppercase == 'y':
        s += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_symbols == 'y':
        s += "!$%&'()*+,-./:;<=>?@[]^_`{|}~"
    
    p = "".join(random.sample(s, passlen))
    print("Complex password generated: ", p)

while True:
    try:
        num = int(input("Enter 1 or 2: "))
        if num not in [1, 2]:
            raise ValueError("Invalid input. Please enter 1 or 2.")
        break
    except ValueError as e:
        print(e)

if num == 1:
    generate_simple_password()
elif num == 2:
    generate_complex_password()

