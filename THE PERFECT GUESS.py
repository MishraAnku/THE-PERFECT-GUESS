#---------------------------------------------------------------------------------------------------------------------THE PERFECT GUESS

# you are going to write the program that generates a random number and ask the user to guess it.
# if the players guess is higher than the actual number the program displays " lower number please".
#  similarly if the user guess it low then program prints higer number please . 
# when the user guess the correct number the program displays the number of guess the player used to arrive at the number .
# hint: use the random module.

import random

number=random.randint(1,100)
attempt=1
guess=int(input("guess the number :"))

while(True):
    if(guess>number):
        guess=int(input("guess another number. this one is too big :"))
        attempt +=1
    elif(guess<number):
        guess=int(input("guess another number. this one is too less :"))
        attempt+=1
    else:
        print(f"yeah thats the number! you guessed it right in {attempt} attempts") 
        break 