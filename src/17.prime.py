'''
3. Write a program to determine if a number, given on the command line, is prime.
'''

number = int(input('Please enter an integer: '))
divisions = 0
for x in range(number):
    if number % (x + 1) == 0:
        divisions += 1

if divisions == 2:
    print("Number is prime")
else:
    print("Number is not prime")
