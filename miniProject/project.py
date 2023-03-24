students = ["Ahmet Furkan ÇAYIRTEPE", "Ayşenur EKİZ", "Berkant AĞUR", "Beyza BİRYOL",
            "Beyza ERDEMİR", "Kaan PULAT", "Petek İŞ"]

def addStudent():
    
    stName = input("Please enter the name of the student to be added to the students list: ")
    stSurname = input("Please enter the surname of the student to be added to the students list: ")

    students.append(stName + " " + stSurname)
    print(f"{stName} {stSurname} has been added to the students list...")
    print(students)

