all_students = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
chess = {1, 2, 3, 4}
robotics = {3, 4, 5, 6, 7}
drama = {8, 9, 10}

print("Finding out the students in chess club :")
for i in chess:
    print("\n.) ",i)

print("")
print("Finding out the students in robotics club :")
for i in robotics:
    print("\n.) ",i)

print("")
print("Finding out the students in robotics or chess club :")
set1 = chess.union(robotics)
print(set1)

print("")
print("Finding out the students in both robotics and chess clubs :")
set2 = chess.intersection(robotics)
print(set2)

set3 = chess.union(drama)

print("Probability formula :")
print("")
print("              Event Outcomes")
print("PROBABILITY = --------------")
print("              Total Outcomes")
print("")
print(f"                                          {len(set1)}")
print(f"PROBABILITY OF CHESS OR ROBOTICS = --------------- = {len(set1)/len(all_students)}")
print(f"                                         {len(all_students)}")
print("")
print(f"                                       {len(set3)}")
print(f"PROBABILITY OF CHESS OR DRAMA = --------------- = {len(set3)/len(all_students)}")
print(f"                                      {len(all_students)}")

tickets = 5
winning = 2
losing = 3

print()
print("==== Independent event ====")
print("\nProbability : ",winning/tickets)

print()
print("==== Dependent event ====")
print("\nProbability : ",winning - 1/tickets - 1)