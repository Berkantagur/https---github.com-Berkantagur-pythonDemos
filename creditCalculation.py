rate = 1.53
term = "24"
creditName = "Education Credit"

print(type(rate))
print(type(term))
print(type(creditName))

print(int(term) + 12)
#print(str(creditName))
rate = str(rate)
print(type(rate))

term = input("Please enter the number of terms that you want: ")
print(term)
print(type(rate))
print(int(term) + 12)

#string interpolation
print("The term that arises as a result of your choice: " + term)
print("The term that arises as a result of your choice:  {newTerm}".format(newTerm = term))

name = "Berkant"
text = "Hello {names}".format(names = name)
print(text)

#f-string
text = f"Welcome {name}"
print(text)