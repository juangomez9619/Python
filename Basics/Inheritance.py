class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am a {self.name} and I am {self.age} years old")


class Cat(Pet):
    def __init__(self, name, age, color):  # overrides constructor
        super().__init__(name, age)  # super Class
        self.color = color

    def speak(self):
        print("meow")

    def show(self):
        print(f"I am a {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):  # overrides the same method in Pet class
        print("bark")


p = Pet("tim", 19)
c = Cat("Bill", 34, "Brown")

c.show()