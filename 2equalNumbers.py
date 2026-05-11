def CheckIfSame(number1, number2):
    if ((number1 ^ number2) != 0):
        print("Numbers are not equal")
    else:
        print("Numbers are equal")

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

CheckIfSame(number1, number2)