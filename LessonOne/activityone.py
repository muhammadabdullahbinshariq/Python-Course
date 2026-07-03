print("What is the type of above given database - \n 1) Relational database \n 2) Non Relational database")
answer = int(input("Enter your choice: "))
while True:
    if answer == 2:
        print("\nYou are correct!")
        print("Please tell your mentor why you chose this")
        break
    elif answer > 2:
        print("\nNo such choice! Run the code and try again")
        break
    else:
        print("\nYou are wrong! The database is a non relational database")
        print("Please tell your mentor why you chose this")
        break