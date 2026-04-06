while True:
    num = int(input("Enter a number: "))
    if num > 9:
        same_str = str(num)
        length = float(len(same_str))
        final = 0
        for digit_char in same_str:
            digit = int(digit_char)
            final += digit**length
        if final == num:
            print(f"{num} is an armstrong number.")
            break
        else:
            print(f"{num} is not an armstrong number.")
    else:
        print("Number is too small. Re-enter the number...")