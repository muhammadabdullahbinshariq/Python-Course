class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Hi my name is {self.name}, and my age is {self.age}")

    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Hi my name is {self.name}, and my age is {self.age}")

    def make_sound(self):
        print("Bark")

cat1 = Cat("Dodo", 2.5)
dog1 = Dog("Tyson", 8)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()