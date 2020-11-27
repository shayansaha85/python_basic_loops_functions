# Python Program to Display the multiplication Table
number = int(input("Enter a number = "))
print("Multiplication table of {0} is".format(number))

for i in range(1,11):
    print("{0} * {1} = {2}".format(number,i,number*i))