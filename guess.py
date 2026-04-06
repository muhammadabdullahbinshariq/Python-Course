import random
print("THE NUMBER GUESSING GAME!")
numbers = []
while True:
    x = input("\nDo you want to add a number? (y/n): ")
    if x == 'y':
        num = float(input("\nEnter your number: "))
        numbers.append(num)
        continue
    elif x == 'n':
        if len(numbers) >= 5:
            break
        else:
            print("\nError! You have added an inssuficient ammount of numbers. Add more.")
            continue
    else:
        print("\nError!")
        continue
if numbers:
    choose = random.choice(numbers)
    print("\nNumber selected! Start guessing.")
    while True:
        guess = float(input("\nEnter your guess: "))
        if guess < choose:
            print("Too low! Try a bigger number.")
        elif guess > choose:
            print("Too high! Try a smaller number.")
        else:
            print("Bingo!")
            print("These are the number(s):", numbers)
            break
else:
    print("No numbers added.")