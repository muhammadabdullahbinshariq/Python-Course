def LCM(num1, num2):
    orig1 = num1
    orig2 = num2
    
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2        
        num2 = remainder   
    
    hcf = num1             
    
    product = orig1 * orig2
    lcm = product // hcf

    print(f"\nThe Lowest Common Multiple of {orig1} and {orig2} is {lcm}")

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
LCM(num1, num2)