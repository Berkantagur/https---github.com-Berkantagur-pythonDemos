class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


customer1 = Person("Engin","Demiroğ")
customer2 = Person("Kerem","Varış")
customer3 = Person("Berkant","Ağur")

print(customer1.name + " " + customer1.surname)
print(customer2.name + " " + customer2.surname)
print(customer3.name + " " + customer3.surname)