# Python program to solve quadratic equation
# sample equation : ax² + bx + c
import cmath

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = cmath.sqrt(b*b - 4*a*c)

ans1 = (-b+d)/(2*a)
ans2 = (-b-d)/(2*a)

print("Quadratic equation")
print("{0}x² + {1}x + {2}".format(a,b,c))
print()
print("x = {0}, {1}".format(ans1,ans2))