# Python Program to Print the Fibonacci sequence
terms = int(input("Enter the number of terms = "))
n1 = 0
n2 = 1
c = 2
if terms==1:
    print(n1)
elif terms==2:
    print(n1," ",n2)
elif terms==0:
    print("")
elif terms>2:
    print(n1,n2,end=" ")
    n3 = n1 + n2
    while c<terms:

        print(n3,end=" ")
        n1 = n2
        n2 = n3
        n3 = n1+n2
        c+=1

