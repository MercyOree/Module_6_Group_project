#Mercy Oreoluwa Koku, Stevn Warn and Ana Escamilla
#Nov/12/2022
#This program is guessing program that will take a number and ramdomly with a random given number.

import random

num = (random.randint(1, 10))
guess = int(input("lets play high/low, I'm thinking of a number between 1-10:"))
if guess < num:
   print ("Higher!")
   guess = int(input("Enter another number:"))
elif guess > num:
   print ("Lower!")
   guess = int(input("Enter another number:"))
elif guess == num:
   print ("Congratulations! You are Correct")
else:
   print ("Sorry but you didn't guess right")
