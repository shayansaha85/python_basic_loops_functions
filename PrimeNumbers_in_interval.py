# Python Program to Print all Prime Numbers in an Interval

def isPrime(number):
    count=0
    for i in range(2, number + 1):
        if number % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


start = int(input("Start point = "))
end = int(input("End point = "))

print("Prime numbers between {0} to {1} :".format(start,end))
for i in range(start,end+1):
    if isPrime(i):
        print(i)