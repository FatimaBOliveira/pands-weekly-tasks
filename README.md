# Programming and Scripting: Weekly Tasks

To write this README, I considered the [Github](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) details regarding README files, what it should contain.

## What the project does

The purpose of this repository is to answer the weekly tasks proposed in the Module Programming and Scripting of the Course Data Analytics in [ATU Galway Mayo](https://www.gmit.ie/). This README contains a brief explanation of the weekly tasks, and for a detailed analysis please check each python script.

## Why the project is useful

Every week, the weekly tasks helped me to put into practice the contents learned and my ability to search information in reliable sources to resolve the problems raised.

## How users can get started with the project

To run this weekly tasks, [Anaconda](https://www.anaconda.com/) and [Visual Studio Code](https://code.visualstudio.com/) need to be installed to run these programs.

## Where users can get help with your project

If there's any issues with the programs, please contact me in the [issues](https://github.com/FatimaBOliveira/My-Data-Analytics-Project/issues) link in my repository.

## Author

Fatima Oliveira

Email:g00438857@atu.ie or Fatima.21.00@hotmail.com
***********************************************************************************

## Week 1 - [helloworld.py](helloworld.py)
- Simple program that prints Hello World!

Print function is enough to run any sentence:
```
print("Hello World!")
```
Or I can use a variable with a string to print it:
```
a = "Hello World!"
print(a)
```
## Week 2 - [bank.py](bank.py)
- Bank is a program that will do the sum of two amounts in cents and read it in euros.

Input int function for the user prompt any amount in cents. I raise a Value Error in case that the user input negative numbers so I can only sum amounts and not subtract them. Then I need to calculate the sum, by adding the amounts and divide it by 100, so I can get the amount in euros. To get the final answer, I need to print the result of the calculation and to print the euro sign I can use the [chr()](https://docs.python.org/3/library/functions.html#chr) function.
```
a = (int(input("Enter amount1(in cent): ")))
b = (int(input("Enter amount2(in cent): ")))
if a<0 or b<0:
    raise ValueError ("The amount has to be positive")
sum = ((a + b) / 100)
print(f" The sum of these is: {chr(8364)}{sum}.")
```
## Week 3 - [accounts.py](accounts.py)
- This program will print out bank account numbers with only the 4 digits showing.

The account number with known number can be treated as a string, so in that way I can use the [replace function](https://www.w3schools.com/python/ref_string_replace.asp) to write the first 6 numbers, and then replace them with 6 X. When I print, it will only show the last 4 digits and the first 6 are replaced with X. I can't treat the number as an int because otherwise replace function cannot be applied.
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

For this task I need to define the Collatz. The [while](https://www.w3schools.com/python/python_while_loops.asp) a !=1 -> [yield](https://docs.python.org/3/reference/expressions.html#yieldexpr) a will process all numbers that are higher than 1 and yield 1 will stop the function. So if a is higher than 1 and even, then I can divide it by 2 and the remainder will be zero. If remainder is not zero, then a is odd and machine will do the calculations as represented in each case. I use a [for loop](https://wiki.python.org/moin/ForLoop) because the program has to run many times as necessary until a = 1. Then I request machine to print the sequence and [end=" "](https://realpython.com/lessons/sep-end-and-flush/) will show them together in single line.
```
a = int(input("Please enter a positive integer: "))
def collatz(a):
    while a != 1:
        yield a 
        if a % 2 == 0:
            a = a // 2 
        else: 
            a = 3 * a + 1
    yield 1
for sequence in collatz(a):
    print(sequence, end=" ")
```
## Week 5 - [weekday.py](weekday.py)
- Machine will check and tell the user if today is a weekday or weekend.

I need to import date from the module [datetime](https://realpython.com/python-datetime/#using-the-python-datetime-module) and call today with function [date.today()](https://docs.python.org/3/library/datetime.html#datetime.date.today) to allow machine to know the current date. The function [today.weekday()](https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python) will process [today's date](https://docs.python.org/3/library/datetime.html#datetime.date.weekday), then it will return a value from 0 to 6, 0 correspondent to Monday and 6 a Sunday. The machine will check which [condition](https://www.w3schools.com/python/python_conditions.asp) is valid and then print it.
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
- Program that will check a positive floating number and will show the an approximation of its square root, using the Newton's Method.

For this task I will ask the user to input a positive number, as negative numbers don't have square roots. The Newton's Method calculation to get the [square root](https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/) is: root = 0.5 * (x + (number/x)). To get x, I need to multiply the number inputted by 0.5. I use a [while loop](https://www.w3schools.com/python/python_while_loops.asp), so the function runs only when the condition is true, root not equal to x. Then I [return](https://realpython.com/python-return-statement/) the root to close the loop, and for the final answer I request the machine to print the number that was square rooted and the result of it [rounded](https://www.w3schools.com/python/ref_func_round.asp) in 1 decimal point.
```
number = float(input("Please enter a positive number: "))
x = 0.5 * number
def sqrt (number, x):
    root = 0.5 * (x + (number/x))
    while root!=x:
        x=root
        root = 0.5 * (x + (number/x))
    return root

print(f"The square root of {number} is approx. {round(sqrt(number, x), 1)}.") 
```
## week 7 - [es.py](es.py)
- Program that will download the Moby Dick book through the internet and counts the number of e's that it contains.

In this task, I searched in Google for the Moby Dick book as [txt](https://www.gutenberg.org/files/2701/old/moby10b.txt) file, and I use the urlretrieve from the [urllib](https://realpython.com/python-download-file-from-url/#using-urllib-from-the-standard-library) package to load it in the program. Then I request the machine to read the txt file with the command-line argument [file handling](https://realpython.com/python-command-line-arguments/#file-handling), and then [return](https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/) the letter counts. Finally I print the argument specifying how many times the letter "e" appears on the file.
```
from urllib.request import urlretrieve
url = (
    "https://www.gutenberg.org/files/2701/old/moby10b.txt"
)
FILENAME = "moby-dick.txt"
urlretrieve(url, FILENAME)

def letterFrequency(FILENAME, letter):
    f = open(FILENAME, 'r')
    text = f.read()
    return text.count(letter)
print(letterFrequency(FILENAME, 'e')) 
```
[Inside](es.py) of this weekly task I also show how to handle with errors such as no argument, non existing files and opening files that are not txt files.

## Week 8 - [plottask.py](plottask.py)
- Program that plots a histogram with normal distribution and a function.

The purpose of this task is to show a histogram with normal distribution of 1000 values with the mean of 5 and deviation of 2 and plot function h(x)= x^3 with range between 0 and 10, both represented in one set of axes. For this I need to divide this task in 2 parts, one with the histogram and other with the function:

To get the histogram, I need to use [numpy random normal function](https://www.w3schools.com/python/numpy/numpy_random_normal.asp), and then only use the [plot.hist function](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html).
```
normaldist = np.random.normal(loc=5, scale = 2, size=1000)
plt.hist(normaldist, label = "Histogram", edgecolor="black")
```
For the function h(x)=x^3 with range between 0 and 10, I use the [numpy arange function](https://realpython.com/how-to-use-numpy-arange/#return-value-and-parameters-of-nparange). I identify h(x) as y because python won't accept the writing form of h(x) as a [variable](https://www.w3schools.com/python/python_variables_names.asp), so I will call it y instead. So y is equal to x cubed so X multiplied by itself and then itself again. Then to represent, I only use the [plt.plot function](https://www.w3schools.com/python/matplotlib_plotting.asp).
```
x = np.arange(0,11) 
y = x * x * x
plt.plot(x, y, label ="x cubed", color = "red")
```
To add [title](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.title.html), [legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html) and name of [axes](https://www.w3schools.com/python/matplotlib_labels.asp), I use the code below, and finally I plot both together with [plt.show()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html).
```
plt.legend()
plt.title("Histogram of normal distribution and x cubed")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
```
***
## End