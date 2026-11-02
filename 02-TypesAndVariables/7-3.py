###
# A program that checks whether the number entered
# from the keyboard is even.
# A number is even if the remainder when divided by 2 is 0.
# The remainder of division is calculated with the % operator.
#
number = int(input('Enter number: '))
even = number % 2 == 0
print(f'Number is even: {even}')