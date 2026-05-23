num = 10
primes = []

while num < 100:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.append(num)
    num += 1

print("The prime numbers from 10 till 99 are:")
for i in primes:
    print(f".) {i}")