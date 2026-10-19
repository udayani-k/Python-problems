#Number guessing game
import random
print("welcome to number guessing game")
number=random.randint(1,10)
guess=0
while guess!=number:
    guess=int(input("enter a numer:"))

    if guess < number:
        print("too low try again")
    elif guess > number:
        print("too high try again")
            
    else:
        print("congratulations")
