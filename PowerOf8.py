def ComputePower(num):
    mask = 1227133513
    result = mask & num
    result ^= num
    if result != 0 or num == 1:
        print(f"\n{num} is not a power of 8.")
    else:
        print(f"\n{num} is a power of 8.")

num = int(input("Enter a number to check if it is a power of 8: "))
ComputePower(num)