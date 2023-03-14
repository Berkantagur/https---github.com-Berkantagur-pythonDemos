#A program that analyzes the letters and numbers of the entered data.

data = "Bazı güzellikler ve hoş şeyler unutulmamalıdır,yoksa dünya yaşanmaya değmezdi 13.03.2023"

newList = list(data)

letterCounter = 0
numberCounter = 0 

for i in newList:
    
    if str(i).isdecimal():
        numberCounter += 1

    else:
        letterCounter += 1

print("Number of characters: ", numberCounter + letterCounter)
print("NUmber of numbers: ", numberCounter)
print("Number of letters: ", letterCounter)
