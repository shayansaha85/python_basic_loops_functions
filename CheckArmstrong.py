# Python Program to Check Armstrong Number
def checkArmstrong(number):
    temporary = int(number)
    result = 0
    while number!=0:
        remainder = number%10
        result += pow(remainder,len(str(temporary)))
        number = number//10

    if temporary==result:
        return True
    else:
        return False


number = int(input("Enter a number = "))
if checkArmstrong(number):
    print("Armstrong")
else:
    print("Not armstrong")