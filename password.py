import random
import string

def generate_password(length):
    temp = string.ascii_lowercase
    password = ''.join(random.choice(temp) for i in range (length))
    print("Randomly generated password is: ", password)


generate_password(9)
generate_password(12)
generate_password(8)
generate_password(14)
generate_passowrd(15)
generate_password(25)