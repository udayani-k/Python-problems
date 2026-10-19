#password generator
import random
import string
def generate_password(length):
    char=string.ascii_letters+string.digits+string.punctuation
    password=""
    for i in range(length):
        password=password+random.choice(char)
    return password
length=int(input("enter password length:"))
password=generate_password(length)
print(password)
     
