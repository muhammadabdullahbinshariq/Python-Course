def OddOcurance(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res

arr = []
size = int(input("Enter the size of your array: "))
while (size):
    element = int(input("Enter your number: "))
    arr.append(element)
    size -= 1

print(f"\n\nOdd Occuring number is {OddOcurance(arr)}")