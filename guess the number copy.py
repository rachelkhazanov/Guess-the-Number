import random
number = (random.randint(0,100))
guess = input('Welcome! Guess my number from 1 to 100: ')
gameFinished = False

while(not gameFinished):
    if (guess == number):
        print "Yes! That's Correct!"
        gameFinished = True
    elif (0 < guess < number):
        guess = input('Sorry, guess higher:') 
    elif (100 > guess > number):
        guess = input('Sorry, guess lower:') 
    elif (guess < 1):
        guess =  input('Please keep guesses between 1 and 100:') 
    elif (guess > 200):
        guess = input('Please keep guesses between 1 and 100:') 
    else: 
        guess = input('Please keep guesses between 1 and 100:')

print "You're FINISHED!"
    
