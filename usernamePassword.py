#Login system according to user name and password.
#NOTE: The user name and password can be changed in the corresponding code line.

username = input("Please enter the username: ")
password = input("Please enter the password: ")

if username == 'admin' and password == 'password':
    print("The entry was successful...")

else: 
    print("The entry failed!!!")
