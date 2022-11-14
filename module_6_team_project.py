#Mercy Oreoluwa Koku, Stevn Warn and Ana Escamilla
#Nov/12/2022
#This program is guessing program that will take a number and ramdomly with a random given number.

import random
number = random.choice


# number == 3
input("enter any number from 1 to 10 by guessing: ")
if number == 3:
    number = "This guess is correct"
    print("You did guessed it")
elif number >= 3:
    number = "This guess is incorrect"
    print("Your guess is to low, Guess higher")
    input("enter any number from 1 to 10 by guessing: ")
elif number <= 3:
    number = "This guess is incorrect"
    print("You guess is to high, Guess low")
    input("enter any number from 1 to 10 by guessing: ")




