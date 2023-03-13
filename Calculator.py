# CALCULATOR

operation = input("Please select the operation you want to perform (+ - / *): ")

if operation == '+' or operation == '-' or operation == '/' or operation == '*' :
        
    number1 = input("Please enter the first integer number: ")
    number2 = input("Please enter the second integer number: ")

    if operation == '+':
        result = int(number1) + int(number2)

    elif operation == '-':
        result = int(number1) - int(number2)

    elif operation == '/':
        result = int(number1) / int(number2)

    elif operation == '*':
        result = int(number1) * int(number2)

    print("Result: ", result)

else :
    print("Invalid operation! Please select valid operation (+ - / *)...")