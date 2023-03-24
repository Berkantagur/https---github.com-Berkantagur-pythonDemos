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

    print(colored("\t~~~~~~REMOVING STUDENT TO THE STUDENT LIST~~~~~~", "light_red"))
    print(students)
    stFullName = input("Please enter the full name of the student to be removed to the students list: ")

    students.remove(stFullName)
    print(colored(f"{stFullName} has been removed to the students list...", "light_green"))
    print(students)

removeStudent()