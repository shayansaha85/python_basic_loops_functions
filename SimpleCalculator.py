# Python Program to Make a Simple Calculator

def calculate(calculations):
    integers = []
    if "+" in calculations:
        integers = calculations.split("+")
        print("=",int(integers[0])+int(integers[1]))
    elif "-" in calculations:
        integers = calculations.split("-")
        print("=",int(integers[0])-int(integers[1]))
    elif "/" in calculations:
        integers = calculations.split("/")
        print("=",int(integers[0])/int(integers[1]))
    elif "*" in calculations:
        integers = calculations.split("*")
        print("=",int(integers[0])*int(integers[1]))
    else:
        print("Invalid calculations")

print("Enter calculations below (e.g. 5+3)")
calculations = input("= ")
calculate(calculations)