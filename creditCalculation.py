creditRate = 1.53
term = "24"
money = 10000
creditName = "Education Credit"

print(type(creditRate))
print(type(term))
print(type(money))
print(type(creditName))

rate = money * 0.10 * (int(term)/12)
print("Rate:" + str(rate))

totalPayment = rate + money
print("Total Money:" + str(totalPayment))










term = input("Please enter the number of terms that you want: ")
print(term)
print(type(rate))
print(int(term) + 12)

#string interpolation
print("The term that arises as a result of your choice: " + term)
print("The term that arises as a result of your choice:  {newTerm}".format(newTerm = term))
print(f"The term that arises as a result of your choice: {term}")

name = "Berkant"
text = "Hello {names}".format(names = name)
print(text)

#f-string
text = f"Welcome {name}"
print(text)
