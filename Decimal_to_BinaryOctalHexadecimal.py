# Python Program to Convert Decimal to Binary, Octal and Hexadecimal

def decimalToBinary(number):
    i = 1
    binary = 0
    while number != 0:
        remainder = number % 2
        number = number // 2
        binary = binary + remainder * i
        i = i * 10
    print(binary)


def decimalToOctal(number):
    i = 1
    octal = 0
    while number != 0:
        remainder = number % 8
        number = number // 8
        octal = octal + remainder * i
        i = i * 10
    print(octal)


def decimalToHexadecimal(number):
    hexcodes = {
        10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
    }
    i = 1
    hex = ""
    while number != 0:
        remainder = number % 16
        number = number // 16
        if remainder < 10:
            hex += str(remainder)
        else:
            hex += hexcodes[remainder]
    print(hex[::-1])


decimalToBinary(13)
decimalToOctal(173)
decimalToHexadecimal(7521)
