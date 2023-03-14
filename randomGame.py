#The game of guessing a randomly selected number with directions
import random 

randomNumber = round(random.random()*100)

# print(randomNumber)

enteredNumber = int(input("Please enter a number between from 1 to 100: "))

while randomNumber != enteredNumber:
    
    if enteredNumber > randomNumber:
        print("You have entered a big number...")

    else:
        print("You have entered small number...")

    enteredNumber = int(input("Please enter a number between from 1 to 100: "))

print("Congratulations, you have won the game :)")