class Expression:
    def __init__(self, val):
        self.val = val

a = Expression(int(input("Enter first number: ")))
b = Expression(int(input("Enter second number: ")))
c = Expression(int(input("Enter third number: ")))
print("The answer to ",a + b + c," is:", a.val + b.val + c.val)