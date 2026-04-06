numberLargest = int(input("Enter Largest number: "))
numberSmallest = int(input("Enter Smallest number: "))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print(f"HCF is {numberLargest}")