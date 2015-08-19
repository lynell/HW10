import random
def get_randomdigit_lastname1lastname2(length):
    i = 0
    code = ''
    while i< int(length):
        digit = str(random.randint(0,9))
        code += digit
        i += 1    
    return code
    
def main():
    print get_randomdigit_lastname1lastname2(3)

main()
