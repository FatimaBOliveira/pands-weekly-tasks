# Bank
# Bank operation that sums two amounts in cents and outputs the sum transaction in euros.
# Author: Fatima Oliveira

a = (int(input("Enter amount1(in cent): ")))
b = (int(input("Enter amount2(in cent): ")))
sum = ((a + b) / 100) # 1 euro is equivalent to 100 cent, so if we divide the sum by 100, we will get the sum in euros.
print(f" The sum of these is: {chr(8364)}{sum}.") 
# To print the euro sign without using the actual sign we can use the chr() function.
# https://docs.python.org/3/library/functions.html#chr