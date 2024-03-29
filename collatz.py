# Collatz
# Program that uses a positive integer and outputs the successive values of the following calculations: 
    # take the current value and, if even, divide it by two, but if it's odd, multiply it by three and add one.
    # Program will end if current value is one
# Author: Fatima Oliveira

a = int(input("Please enter a positive integer: "))

# Will use def to define the collatz so machine can run through it with the following conditions of a.
# https://realpython.com/defining-your-own-python-function/#function-calls-and-definition
def collatz(a):
    while a != 1:
        yield a # "yield" funcion will make the "a" repeat itself but with the new number obtained. This will continue until the sequence it's over when it reaches 1 as defined below.
        if a % 2 == 0: # Even number
            a = a // 2 
        else: 
            a = 3 * a + 1 # Odd number
    yield 1 # yield finishes when the number is 1
# https://docs.python.org/3/reference/expressions.html#yieldexpr
# https://sentry.io/answers/python-yield-keyword/#the-yield-keyword
    
# Generate and print the collatz sequence:
for sequence in collatz(a): # the function "for" will check all the numbers obtained in collatz(a)
    print(sequence, end=" ") # to print all the numbers from function "for". "End=" will show them together in one line
# https://wiki.python.org/moin/ForLoop
# https://realpython.com/lessons/sep-end-and-flush/