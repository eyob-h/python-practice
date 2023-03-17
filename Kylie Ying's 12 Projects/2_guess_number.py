import random


def guess():

    randomNumber = random.randint(1,10)
    guess = 0
    while guess != randomNumber:
        
        guess = int(input("Guess a number between 1 and 10\n"))
        if guess < randomNumber:
            print ("Number too low, guess again")
        elif guess > randomNumber:
            print ("Number too high, guess again")
    
    print(f"You have guessed the correct number {randomNumber}")

guess()

def computerGuess():
    pass
