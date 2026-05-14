def computerPower(x, y):
    result = 1
    while (y > 0):
        if (y % 2 == 0):
            x = x * x
            y >>= 1

        else:
            result = result * x
            y = y - 1
    return result

x = int(input("Enter 'x' for calculating 'x' raised to the power of 'y': "))
y = int(input("Enter 'y' for calculating 'x' raised to the power of 'y': "))
print(f"\nTotal : {computerPower(x, y)}")    