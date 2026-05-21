def myfunction(n):

    first_loop_iterations = 0
    second_loop_iterations = 0
    third_loop_iterations = 0

    for i in range(0, n+1):
        first_loop_iterations += 1
 
    j = 1
    while(j <= n + 1):
        second_loop_iterations += 1
        j = j * 2
 
    for i in range(0,100):
        third_loop_iterations += 1

    print(f"First Loop:\n.) Iterations : {first_loop_iterations}\n.) Complexity : BigO(n)")
    print(f"\nSecond Loop:\n.) Iterations : {second_loop_iterations}\n.) Complexity : BigO(log(n))")
    print(f"\nThird Loop:\n.) Iterations : {third_loop_iterations}\n.) Complexity : BigO(1)")

n = int(input("Enter any number: "))
myfunction(n)