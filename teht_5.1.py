import time
import random

input("How many dice to roll?")
roll_again = "yes"

while roll_again == "yes":
    print("/nRolling the dice...")
    time.sleep(1)

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("The values are: ")
    print("Dice 1 = ", dice1)
    print("Dice 2 =", dice2)

