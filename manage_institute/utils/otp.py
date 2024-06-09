import random
import string

def generate_otp(length = 6):
    otp = ''
    for i in range(length):
        otp  += str(random.randint(1,9))
    return otp



if __name__ == '__main__':
    print(generate_otp(4))














    