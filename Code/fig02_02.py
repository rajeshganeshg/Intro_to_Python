# fig02_02.py
"""Find the minimum of three values."""

number1 = int(input('Enter the first integer: '))
number2 = int(input('Enter the second integer: '))
number3 = int(input('Enter the third integer: '))

minumum = number1

if number2 < minumum:
    minumum = number2

if number3 < minumum:
    minumum = number3

print('Miminum value is', minumum)