# Python Program to Find LCM of a list of numbers

def find_lcm(list):
    def numberOfSuccessfulDivision(list1):
        list1.sort()
        count = 0
        largest = list1[-1]
        for i in range(0, len(list1)):
            if largest % list1[i] == 0:
                count += 1
        return count

    list.sort()
    length = len(list)
    l = list[-1]
    counter=2
    count = numberOfSuccessfulDivision(list)
    if count == length:
        print("LCM = ", list[-1])
    elif count < length:
        while count != length:
            list.pop()
            p = l*counter
            counter=counter+1
            list.append(p)
            count = numberOfSuccessfulDivision(list)
        print("LCM = ", p)


n = int(input("How many numbers you want to enter? = "))
l = []
for i in range(0,n):
    el = int(input("Enter number {0} = ".format(i+1)))
    l.append(el)

find_lcm(l)

