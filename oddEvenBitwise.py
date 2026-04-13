def isEvenOdd(n):
    if (n ^ 1 == n + 1):
        return True; 
    else:
        return False;

number = int(input("Enter your number: "))

if isEvenOdd(number):
    print(f"{number} is even")
else:
    print(f"{number} is odd")