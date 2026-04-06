import math
import random

# Fixed game logic: Ensures the program stops for user input
def play_game():
    while True:
        # 1. Setup the secret number
        x = random.randint(0, 100)
        operate = random.randint(1, 4)
        minus = random.randint(10, 21)
        tries = 5
        
        print(f"\n--- I have chosen a number between 0 and 100 ---")

        # 2. Hints (Calculated once, not in a massive loop)
        if x % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")

        # Prime/Divisibility Check
        is_prime = True
        divisors = []
        for num in range(2, int(math.sqrt(x)) + 1):
            if x % num == 0:
                is_prime = False
                divisors.append(num)
        
        if is_prime:
            print("Hint: The number is a prime number.")
        else:
            # Tell the player a number 'near' a real divisor
            d = random.choice(divisors)
            offset = random.choice([-operate, operate])
            print(f"Hint: The number is divisible by a number near {d + offset}.")

        print(f"Hint: It is bigger than {x - minus}")
        print(f"Hint: It is smaller than {x + minus}")

        # 3. The Guessing Loop (This is where the program STOPS for you)
        while tries > 0:
            try:
                # The input function halts execution until you press Enter
                guess = int(input(f"\n({tries} tries left) Enter your guess: "))
            except ValueError:
                print("That's not a number! Try again.")
                continue

            if guess == x:
                print("Bull's eye! Well done! You're a true maths genius!")
                print(x," is divisible by ",d)
                break # Exit the guessing loop
            else:
                tries -= 1
                if tries > 0:
                    print("Incorrect.")
                else:
                    print(f"Out of lives! The number was {x}.")

        # 4. Restart Logic
        choice = input("\nPlay again? (a: Yes / b: No): ").lower()
        if choice != 'a':
            print("Bye Bye!")
            break

if __name__ == "__main__":
    play_game()