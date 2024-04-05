
import random

def generate_simple_password():
    passlen = 0
    while passlen < 20 or passlen > 92:
        try:
            passlen = int(input("Adja meg a jelszó hosszát (20 és 92 között): "))
            if passlen < 20 or passlen > 92:
                print("A jelszó hossza 20 és 92 karakter közötti lehet.")
        except ValueError:
            print("Helytelen érték, adja meg újra!")

    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&'()*+,-./:;<=>?@[]^_`{|}~"
    p = "".join(random.sample(s, passlen))
    print("Egyszerű jelszó legenerálva: ", p)

def generate_complex_password():
    passlen = 0
    while passlen < 20 or passlen > 92:
        try:
            passlen = int(input("Adja meg a jelszó hosszát (20 és 92 között): "))
            if passlen < 20 or passlen > 92:
                print("A jelszó hossza 20 és 92 karakter közötti lehet.")
        except ValueError:
            print("Helytelen érték, adja meg újra!")
    
    include_symbols = ''
    include_numbers = ''
    include_uppercase = ''
    
    while include_symbols != 'i' and include_numbers != 'i' and include_uppercase != 'i':
        include_numbers = input("Tartalmazzon számokat? (i/n): ").lower()
        include_uppercase = input("Tartalmazzon nagybetűket? (i/n): ").lower()
        include_symbols = input("Tartalmazzon szimbólumokat? (i/n): ").lower()
        
        if include_symbols != 'i' and include_numbers != 'i' and include_uppercase != 'i':
            print("Legalább egy kikötést fogadjon el.")
    
    s = "abcdefghijklmnopqrstuvwxyz"
    
    if include_numbers == 'i':
        s += "0123456789"
    if include_uppercase == 'i':
        s += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_symbols == 'i':
        s += "!$%&'()*+,-./:;<=>?@[]^_`{|}~"
    
    p = "".join(random.sample(s, passlen))
    print("Komplex jelszó legenerálva: ", p)

while True:
    try:
        num = int(input("Adjon meg 1 és 2 közötti számot: "))
        if num not in [1, 2]:
            raise ValueError("Helytelen érték, adja meg újra! ")
        break
    except ValueError as e:
        print(e)

if num == 1:
    generate_simple_password()
elif num == 2:
    generate_complex_password()





