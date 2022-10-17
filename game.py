import random
import time 

print("You and the CPU will get a random number, if you get less than the CPU you will lose \n \n")

time.sleep(3)

yournumber = random.randint(1,100)

cpunumber = random.randint(1,100)

if yournumber >= cpunumber:
    print(f"You got {yournumber} and the CPU got {cpunumber}, you win!")
elif cpunumber > yournumber:
    print(f"You got {yournumber} and the CPU got {cpunumber}, you lose :(")