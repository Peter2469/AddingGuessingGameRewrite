import math
import random
import decimal

print("""Welcome to the game!

-----Description-----
This is a random guessing game which consists from the numbers you give me.
For Example, if you choose 2 and 2, I will choose a number from 0 to 2 and
add the numbers together to get the answer. To win you need to get the 
guessed answer correct.

-----Instructions-----
Pick 2 numbers and then guess what it could be.
----------------------
""")

Digits = []
Choice = input("Please choose 2 numbers, please seperate them with a comma and a space\n")
Replacement = Choice.find(",")
Choice = Choice.replace(", ", "")
Digits.append(Choice[Replacement:])
Digits.append(Choice[:Replacement])

print(f"You gave me {Digits[0]} and {Digits[1]}, the highest the answer can be is {int(Digits[0]) + int(Digits[1])} and the lowest is 0")
Answer = input("What do you think the answer will be?\n")
RandomAnswer = random.randint(0, int(Digits[0])) + random.randint(0, int(Digits[1]))

if int(Answer) == int(RandomAnswer):
    input(f"\nYou chose, {Answer}!\nI chose {RandomAnswer}!\nYou Win")
else:
    input(f"\nYou chose, {Answer}!\nI chose {RandomAnswer}!\nYou Lost")