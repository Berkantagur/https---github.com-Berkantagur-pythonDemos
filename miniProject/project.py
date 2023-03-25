from termcolor import colored

students = ["Ahmet Furkan ÇAYIRTEPE", "Ayşenur EKİZ", "Berkant AĞUR", "Beyza BİRYOL",
            "Beyza ERDEMİR", "Kaan PULAT", "Petek İŞ"]

def addStudent():
    
    print(colored("\t~~~~~~ADDING STUDENT TO THE STUDENT LIST~~~~~~", "light_red"))

    stName = input("Please enter the name of the student to be added to the students list: ")
    stSurname = input("Please enter the surname of the student to be added to the students list: ")

    students.append(stName + " " + stSurname)
    print(colored(f"{stName} {stSurname} has been added to the students list...", "light_green"))
    print(students)

# addStudent()

def removeStudent():

    print(colored("\t\t\t~~~~~~REMOVING STUDENT FROM THE STUDENT LIST~~~~~~", "light_red"))
    print(students)
    stFullName = input("Please enter the full name of the student to be removed to the students list: ")

    students.remove(stFullName)
    print(colored(f"{stFullName} has been removed to the students list...", "light_green"))
    print(students)

# removeStudent()

def addMultiStudent():
    
    print(colored("\t~~~~~~ADDING MORE THAN ONE STUDENT TO THE STUDENT LIST~~~~~~", "light_red"))

    number = int(input("Please enter the number of students that you want to be added: "))
    counter = 0

    while counter<number:

        stFullName = input("Please enter the full name of the student to be added to the students list: ")

        students.append(stFullName)
        print(colored(f"{stFullName} has been added to the students list...", "light_green"))

        counter += 1

    print(students)

# addMultiStudent()

def printStList():

    print(colored("\t~~~~~~PRINTING ALL THE STUDENTS IN THE LIST ONE BY ONE TO THE SCREEN~~~~~~", "light_red"))

    for student in range(len(students)):
    
        print(students[student])
        student += 1

    print(colored("All the students in the list were printed on the screen one by one...", "light_green"))

# printStList()

def learningStudentNo():

    print(colored("\t~~~~~~LEARNING THE STUDENT'S NUMBER~~~~~~", "light_red"))
    
    stFullName = input("Please enter the fullname of the student whose number you want to know: ")
    counter = 0
    
    while counter < len(students):
        
        if students[counter] == stFullName:
            print("{stFullName}'s student number: {counter}".format(stFullName = stFullName, counter = counter))
            break
        
        else:
            counter = counter + 1

# learningStudentNo()

def removeMultiStudent():
    
    print(colored("\t~~~~~~REMOVING MORE THAN ONE STUDENT FROM THE STUDENT LIST~~~~~~", "light_red"))

    number = int(input("Please enter the number of students that you want to be removed: "))
    counter = 0

    while counter<number:

        stFullName = input("Please enter the full name of the student to be removed to the students list: ")

        students.remove(stFullName)
        print(colored(f"{stFullName} has been removed to the students list...", "light_green"))

        counter += 1

    print(students)

# removeMultiStudent()

def operations():

    operation = open("functions.txt", "r")
    print(operation.read())

    choice = int(input("Please choice an operator that you want: "))

    if choice == 1:
        addStudent()

    elif choice == 2:
        removeStudent()

    elif choice == 3:
        addMultiStudent()

    elif choice == 4:
        printStList()

    elif choice == 5:
        learningStudentNo()

    elif choice == 6:
        removeMultiStudent()

        