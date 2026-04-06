subject = ["Mathematics", "Algebra", "Geometry", "Science", "Physics", "Chemistry", "Biology", "English Language", "Literature", "Social Studies", "History", "Geography", "Urdu", "Physical Education", "Art", "Music", "Computer Science", "Technology", "Health", "Maths", "SST", "Bio"]
a = 1
print("The list of available subjects for Grade 8 is:")
for i in subject:
    print(f"{a}. {i}")
    a += 1
file = open("Class.txt", "a")
file.close()
while True:
    file = open("Class.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("Class.txt", "w")
    count = 1
    for line in lines:
        if "|" in line:
            parts = line.split("|", 1)
            content = parts[1].strip()
            file.write(f"{count}. | {content}\n")
            count += 1
    file.close()
    print("\nS.No| Name and Favorite Subject\n-----------------------------------")
    file = open("Class.txt", "r")
    print(file.read().strip())
    file.close()
    ask = input("\nDo you want to make any changes to the datasheet? (y/n): ")
    if ask == "y":
        change = input("What kind of changes? (add/remove): ")
        if change == "add":
            name = input("Enter student name: ")
            fav_sub = input("Enter favorite subject: ")
            if fav_sub not in subject:
                print("Invalid subject!")
                continue
            file = open("Class.txt", "a")
            file.write(f"TEMP | Name : {name} , Fav Subject : {fav_sub}\n")
            file.close()
        elif change == "remove":
            rem_no = input("Enter record number to remove: ")
            file = open("Class.txt", "r")
            lines = file.readlines()
            file.close()
            file = open("Class.txt", "w")
            for line in lines:
                if not line.startswith(rem_no + "."):
                    file.write(line)
            file.close()
        else:
            print("Incorrect entry!")
    elif ask == "n":
        ans = input("Finalize and exit? (y/n): ")
        if ans == "y":
            print("\n--- FINAL DATASHEET ---")
            print("S.No| Name and Favorite Subject\n-----------------------------------")
            file = open("Class.txt", "r")
            print(file.read().strip())
            file.close()
            break
    else:
        print("Incorrect entry!")