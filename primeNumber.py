
number = input("Please specify up to which number the prime numbers are to be written: ")
print("2")

for i in range(3, int(number), 1):
    control = False

    for j in range(2, i):
        if i % j == 0:
            control = True
        
    if control == False:
        print(i)

