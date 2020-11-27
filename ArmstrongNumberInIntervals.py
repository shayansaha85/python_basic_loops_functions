# Python Program to Find Armstrong Number in an Interval

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


def armstrong_in_range(start,end):
    for i in range(start,end+1):
        if checkArmstrong(i):
            print(i)


start = int(input("Enter start point = "))
end = int(input("Enter end point = "))
armstrong_in_range(start,end)