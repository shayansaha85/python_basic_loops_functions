# Python Program to Display Fibonacci Sequence Using Recursion

def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recur_fibonacci(n - 1) + recur_fibonacci(n - 2)


n = int(input("Enter number of terms = "))
for i in range(n):
    print(recur_fibonacci(i), end=" ")
