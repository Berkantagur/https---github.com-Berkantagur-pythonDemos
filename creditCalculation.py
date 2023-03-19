creditRate = 1.53
term = "24"
money = 10000
creditName = "Education Credit"

print(type(creditRate))
print(type(term))
print(type(money))
print(type(creditName))

rate = money * 0.10 * (int(term)/12)
print("Rate:" + str(rate) + "TL")

totalPayment = rate + money
print("Total Money:" + str(totalPayment) + "TL")
