
class Human:

    #self => this
    def greeting(self, sentence):
        print(f"{self.name}: {sentence}")

    def walk(self):
        print(f"{self.name} is walking.")

#instance => örnek
human1 = Human()
human1.name = "Enes"
human1.greeting("Hello", "Berkant")
human1.walk()
