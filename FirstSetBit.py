def Convert(num):
    bits = []
    temp = num
    divide = num // 2
    while (divide != 0):
        divide = temp // 2
        remainder = temp % 2
        remainder = str(remainder)
        bits.append(remainder)
        temp = divide
    bits.reverse()
    bits = "".join(bits)
    print(f"\nNumber : {num}\nBinary Representation : ({bits})\u2082\nPosition of first set bit : {len(bits)}")

num = int(input("Enter any integer: "))
Convert(num)