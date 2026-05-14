def power4(number):
    count = 0
    if (number & (~(number & (number - 1)))):
        while (number > 1):
            number >>= 1
            count += 1
        
        if (count % 2 == 0):
            return True
        else:
            return False
        
number = int(input("Enter the number: "))
if (power4(number)):
    print(f"\n{number} is a power of 4")
else:
    print(f"\n{number} is not a power of 4")