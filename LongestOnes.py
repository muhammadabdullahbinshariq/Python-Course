def LongestOnes(num):
    if num > 0:
        count = 0
        temp = num
        while temp > 0:
            new = temp & (temp << 1)
            temp = new
            count += 1
        print(f"\nThe longest sequence of ones in {num} is : {count}")
    else:
        print(f"\nThere are no ones in {num}")

num = int(input("Enter a number: "))
LongestOnes(num)