# Python Program to Find the Factorial of a Number

def findFactorial(number):
    if number==0:
        return 1
    elif number==1:
        return 1
    else:
        return number * findFactorial(number-1)

number = int(input("Enter a number = "))
print("{0}! = {1}".format(number,findFactorial(number)))