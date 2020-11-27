# Python program to convert Celsius to Fahrenheit

celcius = float(input('Enter temparature in Celcius = '))
fahrenheit = celcius*1.8 + 32
fahrenheit = round(fahrenheit,2)
print("{0}°C = {1}°F".format(celcius,fahrenheit))