
class Human:

    #self => this
    sentence = "Hello"
    def greeting(self):
        print(f"{self.name}: {self.sentence}")

    def walk(self):
        print(f"{self.name} is walking.")

#instance => örnek
human1 = Human()
human1.name = "Berkanr"
human1.greeting("Berkant")
human1.walk()

human2 = Human()
human2.name = "Ahmet"
human2.greeting("Hi", "Kaan")