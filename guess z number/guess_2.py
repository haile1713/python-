import random

def pc_guess (x):
    min =1
    max =x
    feedback =''

    while feedback !='c':
        if min != max:
            guess = random.randint(min,max)
        else :
            guess = max
        feedback = input(f'is {guess} too high(h), too low(l), or correct(c)')

        if feedback =='h' :
            max = guess-1
        elif feedback =='l' :
            min = guess+ 1

    print ("got my number")


pc_guess (1000)
