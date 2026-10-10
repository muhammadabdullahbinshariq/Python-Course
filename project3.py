# Project Three. Date : 10 / 10 / 26. Topic : What Are Your Winning Chances?

tries = int(input("Enter the number of different colour of balls : "))
temp = tries
all_colours = ["White"]

while temp > 0:
    colour = str(input("Enter the colour : "))
    temp -= 1
    all_colours.append(colour)
    if len(all_colours) == tries + 1:
        if len(all_colours) == tries + 1:
            print("List of colours accepted!")
        elif len(all_colours) != tries + 1:
            print("Enter another colour")
            continue
        else:
            print("There is some error!")
            break

all_total = []

for i in all_colours:
    total = int(input(f"Enter the number of total balls for the colour {i} : "))
    all_total.append(total)
    if i == "White":
        temp1 = total
    
all_total = sum(all_total)
print("The total number of balls are :", all_total)

prob1 = (temp1 - 1) / (all_total - 1)
print("Given that the first ball taken out was white, the probability that the second ball will be white is :", prob1)