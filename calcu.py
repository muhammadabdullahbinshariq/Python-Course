print("Simple Calculator:")
while True:
    def add(x, y):
        z = x + y
        print(x ,"+", y , "=", z)

    def sub(x, y):
        z = x - y
        print(x ,"-", y , "=", z)

    def mul(x, y):      
        z = x * y
        print(x ,"x", y , "=", z)

    def div(x, y):
        z = x / y
        print(x ,"/", y , "=", z)

    def mod(x, y):
        z = x % y
        print(x ,"%", y , "=", z)

    def exp(x, y):
        z = x ** y
        print(x ,"^", y , "=", z)

    def fld(x, y):
        z = x // y
        print(x ,"/", y , "is approximately", z)

    def cent(x, y):
        z = (x / y) * 100
        print(x ,"out of", y , "is", z ,"percent")

    print("\nGive the inputs:")
    a = float(input("Enter a number: "))
    b = input("Enter an operation(+,-,*,/,mod,exp,fld,per): ")
    c = float(input("Enter a number: "))

    if b == "+":
        add(a, c)
    elif b == "-":
        sub(a, c)
    elif b == "*":
        mul(a, c)
    elif b == "/":
        div(a, c)
    elif b == "mod":
        mod(a, c)
    elif b == "exp":
        exp(a, c)
    elif b == "fld":
        fld(a, c)
    elif b == "per":
        cent(a, c)
    else:
        print("\nIncorrect operation! Re-enter then operation. Restarting...")