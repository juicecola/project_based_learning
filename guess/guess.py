import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while random_number != guess:
        guess =int(input(f"Guess a number btwn 1 and {x}: "))
        if guess > random_number:
            print("Not it, too high")
           
        elif guess < random_number:
            print("Not it, too low")

        else:
            print(f"Yes its {guess}, you a fucking genious")
guess(10)

