def PrintTwoOdd(arr, size):
    xorof2 = arr[0]
    y = 0
    x = 0
    set_bit = 0
    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]
    set_bit = xorof2 & ~ (xorof2 - 1)
    for i in range(size):
        if (arr[i] & set_bit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    print(f"The two odd elements are {x} and {y}")
arr = []
arr_size = int(input("Enter the size of your array: "))
for i in range(0, arr_size):
    z = int(input("Enetr the element of your array: "))
    arr.append(z)
PrintTwoOdd(arr, arr_size)