# Complete the code to make the HiLo game.

import random

def playHiLo():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101)

    n = int(input("I picked a number between 1 and 100. Can you guess it?"))
    counter = 0
    while n!= secret:
        counter += 1
        if n > secret:
            print ("É um mais BAIXO")
        elif n < secret :
            print ("É um mais ALTO")

        n = int(input("I picked a number between 1 and 100. Can you guess it?"))
    print("Acertaste em ", counter, "tentativas")

    
        


playHiLo()

