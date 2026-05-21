n = int(input("Enter number n : "))
m = int(input("Enter number m : "))

def method1(n, m):
    print(f"\nn x m = {n * m}\nIterations : 1\n")

def method2(n, m):
    iterations = 0
    addition_list = []
    
    # Loop m times to collect n
    for i in range(m):
        addition_list.append(str(n))
        iterations += 1
        
    # Join the numbers with " + "
    addition_sequence = " + ".join(addition_list)
    
    print(f"{addition_sequence} = {n * m}")
    print(f"n x m = {n * m}")
    print(f"Iterations : {iterations}")
    return iterations

method1(n, m)
method2(n, m)