# Bank
# Bank operation that sums two amounts in cents and outputs the sum transaction in euros.
# Author: Fatima Oliveira

a = (int(input("Enter amount 1 (in cent): "))) # Input will ask the user to write a number, an integer.
b = (int(input("Enter amount 2 (in cent): "))) # https://realpython.com/python-input-integer/
if a<0 or b<0:
    raise ValueError ("The amount has to be positive") # Will raise ValueError if the amounts are negative.
sum = ((a + b) / 100) # 1 euro is equivalent to 100 cent, so if we divide the sum by 100, we will get the sum in euros.

print(f" The sum of these is: {chr(8364)}{sum}.") 
# To print the euro sign without using the actual sign we can use the chr() function.
# https://docs.python.org/3/library/functions.html#chr