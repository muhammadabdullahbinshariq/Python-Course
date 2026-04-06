#Activity 1
#Store your Name, Age, Weight, Whether you are a student or not (True for yes, False for no) in respective variables. What do you think is the data type of each variable? Print the data type of every variable. Change the datatype of Age to string and Weight to an integer.
name = "Muhammad Abdullah bin Shariq"#str datatype
age = "13 yrs"#str datatype
weight = "40"#str datatype
print(type(name))
print(type(age))
print(type(weight))
age = str(age)
weight = int(weight)
print(type(age))
print(type(weight))

#Activity 2
#Store two numbers of your choice in two different variables. Now perform all the Arithmetic operations on those two numbers and print the results.
x = input("Enter Number 1: ")
y = input("Enter Number 2: ")
print(x ,"+", y ,"=", x + y)
print(x ,"-", y ,"=", x - y)
print(x ,"*", y ,"=", x * y)
print(x ,"/", y ,"=", x / y)
print(x ,"**", y ,"=", x ** y)
print(x ,"//", y ,"=", x // y)
print(x ,"%", y ,"=", x % y)

#Activity 3
#Store the values of your first name and last name in respective variables. Now add these two strings and store them in the variable full name. Create another variable with the first name multiplied by any number of your choice as its value. Print all the four variables Now add another variable to your program with any string of your choice. Find its length, print its first and last character, and print a sub-string of this original string as well.
first = "Muhammad"
last = "Shariq"
full = first + last