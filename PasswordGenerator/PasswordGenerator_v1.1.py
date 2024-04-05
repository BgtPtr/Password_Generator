#import random
#
#def generate_simple_password():
#    passlen = int(input("Enter the length of password / Adja meg a jelszó hosszát: "))
#
#    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&'()*+,-./:;<=>?@[]^_`{|}~"
#    p = "".join(random.sample(s, passlen))
#    print(p)
#
#
#def generate_complex_password():
#    passlen = int(input("Enter the length of password: "))
#    include_numbers = input("Include numbers? / Tartalmazzon számokat? (y/n): ").lower()
#    include_uppercase = input("Include uppercase letters? / Tartalmazzon nagybetűket? (y/n): ").lower()
#    include_symbols = input("Include symbols? / Tartalmazzon szimbólumokat? (y/n): ").lower()
#    
#    s = "abcdefghijklmnopqrstuvwxyz"
#    
#    if include_numbers == 'y':
#        s += "0123456789"
#    if include_uppercase == 'y':
#        s += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    if include_symbols == 'y':
#        s += "!$%&'()*+,-./:;<=>?@[]^_`{|}~"
#    
#    if not any([include_symbols == 'y', include_numbers == 'y', include_uppercase == 'y']):
#        print("No additional requirements selected for password generation. / Tartalmaznia kell egyet a három feltétel közül.")
#    else:
#        p = "".join(random.sample(s, passlen))
#        print("Complex password generated: ", p)
#
#while True:
#    try:
#        num = int(input("Enter 1 or 2: "))
#        if num not in [1, 2]:
#            raise ValueError("Invalid input. Please enter 1 or 2.")
#        break
#    except ValueError as e:
#        print(e)
#
#if num == 1:
#    generate_simple_password()
#elif num == 2:
#    generate_complex_password()


import random

def generate_simple_password():
    passlen = int(input("Enter the length of password / Adja meg a jelszó hosszát: "))
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&'()*+,-./:;<=>?@[]^_`{|}~"
    p = "".join(random.sample(s, passlen))
    print(p)

def generate_complex_password():
    passlen = int(input("Enter the length of password: "))
    include_symbols = ''
    include_numbers = ''
    include_uppercase = ''
    
    while include_symbols != 'y' and include_numbers != 'y' and include_uppercase != 'y':
        include_symbols = input("Include symbols? (y/n): ").lower()
        include_numbers = input("Include numbers? (y/n): ").lower()
        include_uppercase = input("Include uppercase letters? (y/n): ").lower()
        
        if include_symbols != 'y' and include_numbers != 'y' and include_uppercase != 'y':
            print("At least one of the requirements must be selected.")
    
    s = "abcdefghijklmnopqrstuvwxyz"
    
    if include_symbols == 'y':
        s += "!@#$%^&*()?"
    if include_numbers == 'y':
        s += "01234567890"
    if include_uppercase == 'y':
        s += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
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



