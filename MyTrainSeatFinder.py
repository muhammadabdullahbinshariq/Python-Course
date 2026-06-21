import random

available_seats = []
rand = random.choice(range(1, 3))
temp = rand
while len(available_seats) < 20:
    rand1 = random.choice(range(2, 6))
    rand1 += temp
    available_seats.append(rand1)
    temp = rand1

seat = random.choice(available_seats)
print(f"Seat no. = {seat}")

lo1, hi1, step1 = 0, len(available_seats) - 1, 0
while lo1 <= hi1:
    step1 += 1
    mid1 = (lo1 + hi1) // 2
    if available_seats[mid1] == seat:
        print(f"Seat no. {seat} found at index : {mid1}\nSteps required : {step1}\nComplexity : BigO(1)")
        break
    elif available_seats[mid1] < seat:
        lo1 = mid1 + 1
    else:
        hi1 = mid1 - 1

    if lo1 > hi1:
        print(f"Seat no. {seat} not found")
        break

print(f"\nAvailable seats : {available_seats}")

def find_seat(train, seat, lo2, hi2, steps2 = 0):
    steps2 += 1
    mid = (lo2 + hi2) // 2
    if lo2 > hi2:
        return -1, steps2
    if train[mid] == seat:
        return mid, steps2
    elif train[mid] < seat:
        return find_seat(train, seat, mid + 1, hi2, steps2)
    else:
        return find_seat(train, seat, lo2, mid - 1, steps2)
    
result, steps2= find_seat(available_seats, seat, 0, len(available_seats) - 1)
index_found, total_steps = find_seat(available_seats, seat, 0, len(available_seats) - 1)
print(f"\n{result}\nComplexity : BigO(log n)\nSteps required : {steps2}\nSeat no. {seat} found at index : {index_found}")

print(f"\nAvailable seats : {available_seats}")