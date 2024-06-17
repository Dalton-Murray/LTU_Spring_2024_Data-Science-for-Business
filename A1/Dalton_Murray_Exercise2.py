#####################
## Dalton Murray    #
## 01/31/2024       #
## A1 - Exercise 2  #
#####################
import sys # Required for system functions

import matplotlib as mplib # Imports matplotlib library and sets an alias to mplib
from matplotlib import pyplot as plt # Imports pyplot from matplotlib and sets an alias to plt

# Defines the __main__ function
def __main__():

    temperatureData = [57.56, 61.52, 53.42, 59.36, 65.3, 71.78, 66.92, 77.18, 74.12, 64.58] # Temperature data given to us
    salesData = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421] # Sales data given t ous

    plt.scatter(temperatureData, salesData) # Sets up a scatter plot with x and y as temperatureData and salesData
    plt.xlabel("Degress Fahrenheit") # Sets the x label to Degrees Fahrenheit as that is the data we've been given
    plt.ylabel("Sales Per Day USD") # Sets the y label to Sales USD as this is the amount of sales they had on that day
    plt.title("Frozen Yogurt Sales vs Temperature") # Sets the title of the plot to Frozen Yogurt Sales vs Temperature as that is what this plot is showing
    plt.show() # Shows the plot

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly