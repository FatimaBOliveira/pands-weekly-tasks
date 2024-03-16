# Plot Task
# Program that shows a histogram of a normal distribution and a plot of a funtion.
# Author: Fatima Oliveira

import numpy as np
import matplotlib.pyplot as plt

# Histogram with:
# Normal distribution with 1000 random numbers with the mean of 5 and deviation of 2.
normaldist = np.random.normal(loc=5, scale = 2, size=1000) # https://www.w3schools.com/python/numpy/numpy_random_normal.asp
plt.hist(normaldist, label = "Histagram", edgecolor="black")

# Funtion h(x)=x^3:
# h(x) is represented in the y axe, and x in the x axe.
x = np.arange(0,11)
# The range is between 0 and 10, so 11 needs to be the stop number in order to 10 be included since last number in array is always excluded as explained in https://realpython.com/how-to-use-numpy-arange/#return-value-and-parameters-of-nparange
y = x * x * x
plt.plot(x, y, label ="x cubed", color = "red")
plt.legend()
plt.title("Histagram of normal distribution and x cubed") # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.title.html
plt.xlabel("X") # https://www.w3schools.com/python/matplotlib_labels.asp
plt.ylabel("Y")
plt.show()