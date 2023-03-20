
creditRate = input("Please enter the interest rate: ")
term = input("Please enter the number of terms that you want: ")
money = input("Please enter the principal amount: ")
creditName = "Personal Credit"

creditRate = float(creditRate)
term = int(term)
money = int(money)

rate = money * 0.10 * (term/12)
print("Rate:" + str(rate) + "TL")

totalPayment = rate + money

print("\n\t" + creditName)
print("Total Money: {totalPayment} TL".format(totalPayment = totalPayment))
print(f"Total Money: {totalPayment} TL")
#string interpolation