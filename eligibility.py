working = float(input("Enter the total number of working days: "))
absent = float(input("Enter the number of days you took off: "))
percent = (absent / working) * 100
percent = round(percent)
percent = 100 - percent
print("You attended ",percent,"% of the total working days,", end = '')
if percent >= 75:
    print(" so you are permitted to sit in the exam.")
else:
    print(" so you are not permitted to sit in the exam.")