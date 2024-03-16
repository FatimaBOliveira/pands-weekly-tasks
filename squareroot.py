# Square root
# Program that takes a positive floating-point and outputs an approximation in sqare root.
# Author: Fatima Oliveira

# https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756
number = float(input("Please enter a positive number: "))
x = 0.5 * number
def sqrt (number, x):
    root = 0.5 * (x + (number/x)) # this is the Newton method to get the square root: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
    while root!=x: # Will run as long the condition is true, root not equal to x; https://www.w3schools.com/python/python_while_loops.asp
        x=root
        root = 0.5 * (x + (number/x))
    return root # Return function will finish the def function and return the value to the final code. https://realpython.com/python-return-statement/

print(f"The square root of {number} is approx. {round(sqrt(number, x), 1)}.") # round function to get square root with 1 decimal.
# https://www.w3schools.com/python/ref_func_round.asp