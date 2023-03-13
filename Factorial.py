
factorial = input("Enter the number to be factorized: ")

factor = 1
counter = 1

while int(factorial) + 1 > counter:
    factor *= counter
    counter+= 1

print(factorial,"! =",factor)