def all_subsequences(string):
    length = len(string)
    total = 1 << length
    subsequences_list = []
    
    for mask in range(0, total):
        current_subseq = ""
        for i in range(0, length):
            if (mask & (1 << i)) != 0:
                current_subseq += string[i]
        subsequences_list.append(current_subseq)

    return subsequences_list

n = int(input("How many characters would you like in your string? "))
m = []
for i in range(n):
    o = str(input("Enter your letter: "))
    m.append(o)

result = all_subsequences(m)
print("\nAll generated substrings:")
no = 0
for i in result:
    print(no,".", i)
    no += 1
