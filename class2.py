class student:
    grade = 9
    name = "Muhammad Abdullah bin Shariq"

    def introduction(self):
        print("Hi! I'm a student")

    def details(self):
        print("My name is", self.name)
        print("I study in grade", self.grade)

ob = student()
ob.introduction()
ob.details()