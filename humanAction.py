
class Human:

    #self => this
    name = "Enes"
    def greeting(self, sentence):
        print(f"{self.name}: {sentence}")

    def walk(self):
        print(f"{self.name} is walking.")

#instance => örnek
human1 = Human()
human1.greeting("Hello", "Berkant")
human1.walk()

human2 = Human()
human2.name = "Ahmet"
human2.greeting("Hi", "Kaan")