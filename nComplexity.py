def OnTime(n):
    iterations = 0
    for i in range(1, n + 1):
        iterations += 1
    print(f"When n is {n}, the number of iterations are {iterations}")

OnTime(10)
OnTime(20)
OnTime(42)
print("\nWith every 'n', the time taken and the number of iterations will increase.")