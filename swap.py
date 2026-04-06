while True:
    x = int(input("Enter the number '5': "))
    y = int(input("Enter the number '9': "))
    z = int(input("Enter the number '1': "))

    a = 0

    if not (1 <= x <= 9 and 1 <= y <= 9 and 1 <= z <= 9):
        print("There is an error! Restarting...")
        continue

    if x != 5:
        print("The first number that has been entered is not 5! Restarting...")
        continue
    elif y != 9:
        print("The second number that has been entered is not 9! Restarting...")
        continue
    elif z != 1:
        print("The third number that has been entered is not 1! Restarting...")
        continue

    print("Jumbled values:", x, y, z)

    if x > y:
        a = x
        x = y
        y = a

    if y > z:
        a = y
        y = z
        z = a

    if x > y:
        a = x
        x = y
        y = a

    print("Values in ascending order:", x, y, z)
    break