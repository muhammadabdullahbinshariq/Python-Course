import random
print("THE JUMBLED-WORD GUESSING GAME")
while True:
    words = ["skeptical", "eradicate", "polythiesm", "doomed"]
    # 1. Building the Library
    while True:
        answer = input("Add word to library? (y/n): ").lower()
        if answer == "y":
            word = input("Enter your word: ")
            words.append(word)
        else:
            if not words: # Safety check so game doesn't crash if list is empty
                words = ["python", "coding", "logic"]
            break

    # 2. Setup the Round
    chosen = random.choice(words)
    # This creates a jumbled version of the WHOLE word
    jumbled_list = random.sample(chosen, len(chosen))
    jumble = "".join(jumbled_list)
    
    tries = 5
    
    # 3. The Guessing Loop (Nested so they can try the SAME word)
    while tries > 0:
        print(f"\nJumbled word: {jumble}")
        print(f"Tries left: {tries}")
        guess = input("Can you unjumble it? ")

        if guess == chosen:
            print("Bingo!")
            break
        else:
            tries -= 1 # Corrected way to subtract
            if tries > 0:
                print("Incorrect. Try again!")
            else:
                print(f"Out of tries! The word was: {chosen}")

    # 4. Play Again?
    ask = input("\nPlay again? (y/n): ").lower()
    if ask != 'y':
        print("\nCOME AGAIN! BYE!")
        break