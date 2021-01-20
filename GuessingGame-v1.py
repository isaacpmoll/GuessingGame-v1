#Do Stuff Here


import time
import random

name = input("What is your name? ")
print("Well then, " +name+ ", let's play a guessing game!")
time.sleep(1)
mi = int(input("Pick the minimum range: "))
ma = int(input("Pick the maximum range: "))
ran = random.randint(mi, ma)

guess = int(input("What is your guess? "))

if guess==ran:
	print("correct!")
else:
	print("wrong...")