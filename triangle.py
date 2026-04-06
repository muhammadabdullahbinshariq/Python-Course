#Write a Python program for printing the stars in a pattern using Nested for loop.
rows = int(input("Enter the number of rows you want: "))
for i in range(1, rows+1):
    for j in range(i):
        print("*",end='')
    print()