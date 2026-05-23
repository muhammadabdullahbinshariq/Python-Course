def solveCircuit(a, b, c):
    first = a & b
    second = b | c
    third = c & b
    fourth = second & third
    q = first | fourth
    print(f"\nThe final result is : {q}")

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
solveCircuit(a, b, c)