import random

def play_hangman():
    # Enhanced ASCII art
    man = [" O", "/|\ ", "/ \ "]
    gallows = [" ______| ", " |     | ", " |    "]
    
    words = [
        "apple", "banana", "cherry", "dragonfruit", "elderberry", 
        "fig", "grape", "honeydew", "iceberg", "jackfruit", 
        "kiwi", "lemon", "mango", "nectarine", "orange", 
        "papaya", "quince", "raspberry", "strawberry", "tangerine", 
        "ugli", "vanilla", "watermelon", "xigua", "yam", 
        "zucchini", "mountain", "river", "ocean", "forest", 
        "desert", "valley", "canyon", "island", "glacier", 
        "volcano", "prairie", "tundra", "savanna", "marsh", 
        "swamp", "lagoon", "plateau", "summit", "meadow", 
        "garden", "forest", "jungle", "orchard", "vineyard",
        "castle", "palace", "abnegation", "acquiesce", "alacrity", "anachronism", "arcane",
        "belligerent", "cacophony", "didactic", "ebullient", "ephemeral",
        "fastidious", "garrulous", "iconoclast", "insidious", "juxtapose",
        "loquacious", "magnanimous", "obfuscate", "perfunctory", "ubiquitous"
    ]

    word_str = random.choice(words)
    word_list = list(word_str)
    
    indices = list(range(len(word_list)))
    to_hide = random.sample(indices, len(word_list) // 3)
    
    display_word = list(word_list)
    for idx in to_hide:
        display_word[idx] = "_"

    wrong_tries = 0

    while True:
        for line in gallows:
            print(line)
        for part in man:
            print(part)
        
        print("\nWord: " + " ".join(display_word))
        guess = input("Guess the full word: ").strip().lower()

        if guess == word_str:
            print("✨ Correct! The man survives! ✨")
            break
        else:
            wrong_tries += 1
            print(f"❌ Wrong! ",3 - wrong_tries," tries until he loses a part!")
            
            if wrong_tries == 3:
                if man:
                    removed_part = man.pop() 
                    print(f"⚠️  A part was removed! Remaining parts: {len(man)}")
                    wrong_tries = 0
                
                if not man:
                    print("💀 GAME OVER. The man is gone.")
                    print(f"The word was: {word_str}")
                    break

play_hangman()