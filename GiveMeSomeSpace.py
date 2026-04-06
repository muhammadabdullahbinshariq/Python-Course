def sum_n(n):
    return n * (n + 1) // 2

print("Sum of first n numbers (n = 5):", sum_n(5))

def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total

a = [12, 3, 4, 15]
print(f"\nArray sum: {array_sum(a)}")

def sumn(n):
    if n <= 0:
        return 0
    return n + sumn(n - 1)

print(f"\nRecursive sum (n = 5): {sumn(5)}")