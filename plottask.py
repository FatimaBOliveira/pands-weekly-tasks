# Plot Task
# Program that shows a histogram of a normal distribution and a plot of a funtion.
# Author: Fatima Oliveira

# For this task I need the module Numpy to do get the arrays and Matplotlib to plot.
import numpy as np
import matplotlib.pyplot as plt

# I use Numpy to get a normal distribution of 1000 random numbers with the mean of 5 and deviation of 2.
normaldist = np.random.normal(loc=5, scale = 2, size=1000) # https://www.w3schools.com/python/numpy/numpy_random_normal.asp
# Matplotlib to plot the histogram.
plt.hist(normaldist, label = "Histogram", edgecolor="black") # Plot Histogram with label and edge color.
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html


# The funtion used is h(x)=x^3 with the range between 0 to 10.
# h(x) is represented in the y axe, and x in the x axe.
x = np.arange(0,11)# 11 is the stop number in order to 10 be included in the range since last number in array is always excluded. 
#https://realpython.com/how-to-use-numpy-arange/#return-value-and-parameters-of-nparange
y = x * x * x
plt.plot(x, y, label ="x cubed", color = "red") # plot the function with label and color to represent the function.
# https://www.w3schools.com/python/matplotlib_plotting.asp


# Then to customize the plot
plt.legend() # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
plt.title("Histagram of normal distribution and x cubed") # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.title.html
plt.xlabel("X") # https://www.w3schools.com/python/matplotlib_labels.asp
plt.ylabel("Y")

# And finally I can plot histogram and function together.
plt.show()
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html