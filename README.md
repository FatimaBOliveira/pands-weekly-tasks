# Programming and Scripting: Weekly Tasks

The purpose of this repository is to answer the weekly tasks proposed in the Module Programming and Scripting of the Course Data Analytics in the University of ATU Galway Mayo.
** By Fatima Oliveira**
***********************************************************************************
## Week 1 - [helloworld.py](helloworld.py)
- Simple program that prints Hello World!

Print function is enough to run any sentence:
```
print("Hello World!")
```
## Week 2 - [bank.py](bank.py)
- Bank is a program that will do the sum of two amounts in cents and read it in euros.

Input function for the user to put the any amount in cents. Then I need to calculate, adding the amounts and divide it by 100, so I can get the amouny in euros. To get the final answer, I need to print the result of the calculation and to print the euro sign we can use the [chr()](https://docs.python.org/3/library/functions.html#chr) function.
```
a = (int(input("Enter amount1(in cent): ")))
b = (int(input("Enter amount2(in cent): ")))
sum = ((a + b) / 100) 
print(f" The sum of these is: {chr(8364)}{sum}.")
```
## Week 3 - [accounts.py](accounts.py)
- This program will print out bank account numbers with only the 4 digits showing.

The account number with known number can be treated as a string so then I can use the [replace function](https://www.w3schools.com/python/ref_string_replace.asp) and write the first 6 numbers and then write the 6 X so when I print, in will only show the last 4 digits and the first 6 are replaced with X. I can't treat the number as an int because otherwise replace function cannot be applied.
```
accountnumber = "1234567890"
print ((f"Please enter an 10 digit account number: ") + str(accountnumber))
print (accountnumber.replace("123456", "XXXXXX"))
```
For the extra part of the assessment, I will process number of any length and show only again the last 4 digits. For this I request user to input 2 entries, one as a string so I can use the replace function again and the last 4 digits as an int. In the final part I print both entries.
```
accountnumberA = str(int(input("Please enter the first numbers of your account: ")))
a = (accountnumberA.replace(accountnumberA, "XXXXXX"))
accountnumberB = int(input("Please enter the last 4 numbers of your account: "))
print (f"{a}{accountnumberB}")
```
## Week 4 - [collatz.py](collatz.py)
- Collatz will take an integer and if this is even, it will divide it by two, but if odd, it will multiply it by three and add one. The program will end if the current value is one.

For this task I need to define the Collatz. The while a !=1 -> [yield](https://docs.python.org/3/reference/expressions.html#yieldexpr) a will process all numbers that are higher than 1 and yield 1 will stop the function. So if a is higher than 1 and even, then the remainder will be zero; if remainder is not zero, then a is odd and machine will do the calculations as represented in each case. I use a [for loop](https://wiki.python.org/moin/ForLoop) because the program has to run n times until a = 1.
```
def collatz(a):
    while a != 1:
        yield a 
        if a % 2 == 0:
            a = a // 2 
        else: 
            a = 3 * a + 1
    yield 1
a = int(input("Please enter a positive integer: "))
for sequence in collatz(a):
    print(sequence, end=" ")
```
## Week 5 - [weekday.py](weekday.py)
- Machine will check and tell the user if today is a weekday or weekend.

I need to import the module [datetime](https://realpython.com/python-datetime/#using-the-python-datetime-module) and then I define today to allow machine to know the current date. The function [.weekday](https://docs.python.org/3/library/datetime.html#datetime.date.weekday) will process today's date and check which day of the week it is, then it will return a value from 0 to 6, 0 being a Monday and 6 a Sunday. I will use the print function for the machine to tell me that is weekday if value is between 0 and 4 and weekend if value is 5 or 6.
```
from datetime import date 
today = date.today()
if today.weekday() == 0:
    print("Yes, unfortunately today is a weekday.")
elif today.weekday() == 1:
    print("Yes, unfortunately today is a weekday.")
elif today.weekday() == 2:
    print("Yes, unfortunately today is a weekday.")
elif today.weekday() == 3:
    print("Yes, unfortunately today is a weekday.")
elif today.weekday() == 4:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
```
## Week 6 - [squareroot.py](squareroot.py)
- Program that will check a positive floating number and will show the square root, using the Newton method.

## week 7 - [es.py](es.py)
- Program that will download the Moby Dick book through the internet and counts the number os e's that it contains.

***********************************************************************
# End