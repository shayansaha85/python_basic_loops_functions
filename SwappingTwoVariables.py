# Python program to swap two variables

variable1 = input("Enter a first variable = ")
variable2 = input("Enter second variable = ")

print("Before swapping")
print("variable1 = {0}, variable2 = {1}".format(variable1,variable2))

temporaryVar = variable1
variable1 = variable2
variable2 = temporaryVar

print("After swapping")
print("variable1 = {0}, variable2 = {1}".format(variable1,variable2))