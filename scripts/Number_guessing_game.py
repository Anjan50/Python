# Number guessing game
# By fr4nkl1n-1k3h

import random

tries = 0
try_limit = 5
guesses = []
num = random.randint(1,20)

while tries != try_limit:
    guess = int(input("guess the secret number from 1 - 20: "))
    print(f"\nYou guessed: {guess}")
    guesses.append(guess)
    tries += 1
    
    if guess == num:
        print("\nYOU WIN!!!")
        print(f"The secret number is {num}")
        break
    else:
        if guess in range(num - 5, num) or guess in range(num, num + 5):
            print("your so close, HOT")
        else:
            print("not even close, COLD")
            
    if tries == try_limit:
        print('\n\nyou lose')
        print(f"you guessed {guesses}")
        print(f"the secret number is {num}")
            