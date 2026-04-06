class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
print(blu.species)
print(woo.species)
print(blu.name, blu.age)
print(woo.name, woo.age)