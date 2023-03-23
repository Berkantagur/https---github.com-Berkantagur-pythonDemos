
class Human:

    #self => this
    sentence = "Hello"
    name = "Ali"
    def greeting(self):
        print(f"{self.name}: {self.sentence}")

    def greeting1(self):
        print(f"{self.name}: {self.sentence1}")

#instance => örnek
human1 = Human()
human1.name = "Berkant"
human1.greeting()

human2 = Human()
human2.sentence1 = "Hi"
human2.greeting1()
