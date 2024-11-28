#Number Guessing game
import random
print("Welcome\n")
lower = 0
upper = 100
ran = int(random.randrange(lower,upper))

while True:
    guess = int(input("Enter your guess between (0-100):"))    
    if guess > ran:
        print("Guess a bit lower")
    elif guess < ran:
        print("Guess a bit higher")
    elif guess == ran:
        print("Yhoo! you guessed it right")
        break
    