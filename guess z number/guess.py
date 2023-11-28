import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess !=  random_number:
        guess=int(input("guess a number : "))
        if guess < random_number :
            print ("its too low ")
        elif guess > random_number:
            print ("its too high ")
    print ("tadaaaa guessed correctly ")

guess(10)