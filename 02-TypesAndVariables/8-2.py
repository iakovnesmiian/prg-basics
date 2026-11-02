###
# A program that reads temperature in degrees Celsius from the keyboard.
#

# read temperature in Celsius from the keyboard
celsius = float(input('Enter temperature in Celsius: '))
# Kelvin = Celsius + 273.15
kelvin = celsius + 273.15
# Fahrenheit = Celsius * 9/5 + 32
fahrenheit = celsius * 9 / 5 + 32
# print results
print(f'{celsius} C = {kelvin:.2f} K = {fahrenheit:.2f} F')