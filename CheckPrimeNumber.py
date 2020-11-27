# Python Program to Check Prime Number

def checkPrime(number):
    count=0
    try:
        if number==1 or number==0:
            print("Neither prime nor composite")
        elif number>1:
            for i in range(2,number+1):
                if number%i==0:
                    count+=1
            if count==1:
                print("Prime")
            else:
                print("Not prime")
    except ValueError:
        print("Invalid entry")


number = int(input("Enter a number = "))
checkPrime(number)


