# Python Program to Find the Sum of Natural Numbers
def sum_in_range(end):
    sum = 0
    for i in range(1, end+1):
        sum += i
    print("Result of 1+2+3+.......+{0}".format(end))
    print("= {0}".format(sum))


end = int(input("Enter the limit = "))
sum_in_range(end)