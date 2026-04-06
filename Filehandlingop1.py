with open('Codingal.txt' , 'w') as file:
    file.write("Hi! I am a penguin and I am 1 years old.")

file.close()

with open('Codingal.txt' , 'r') as file:
    data = file.readlines()
    print("Words in this file are......")
    for line in data:
        word = line.split()
        print(word)

file.close()