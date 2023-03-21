
vize = int(input("Please enter your vize mark score:"))
final = int(input("Please enter your final mark score:"))

average = vize * 0.40 + final  * 0.60
print("Your mark average:", average)

if average <= 30:
    print("You are failed!")

else:
    print("Congratulations, You've passed...")