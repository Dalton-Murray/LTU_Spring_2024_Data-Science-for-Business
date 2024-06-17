#####################
## Dalton Murray    #
## 01/31/2024       #
## A1 - Exercise 3  #
#####################
import sys # Required for system functions

import matplotlib as mplib # Imports matplotlib library and sets an alias to mplib
from matplotlib import pyplot as plt # Imports pyplot from matplotlib and sets an alias to plt

# Defines the __main__ function
def __main__():

    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # Create a list of the number for each month

    # Unused data due to not being included in required parts of the exercise, however, I converted it from the given data to lists for future analysis as needed
    # faceCreamData = [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900]
    # faceWashData = [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760]
    # toothPasteData = [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400]
    # bathingSoapData = [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400]
    # shampooData = [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800]
    # moisturizerData = [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760]

    # It is possible for me to make a dictionary for the following two variables however this is a simple way to do is also
    totalUnitsData = [21100, 18330, 22470, 22270, 20960, 20140, 29550, 36140, 23400, 26670, 41280, 30020] # Given data for the total units sold per month
    totalProfitData = [211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200] # Given data for the total profit per month

    # Part A
    plt.plot(months, totalProfitData) # Takes in for a regular line graph the months as x and totalProfitData as y
    plt.title("Total Profit vs. Month") # Sets the tiel to total profit vs month
    plt.xlabel("Month of The Year") # Sets the x label to month of the year
    plt.ylabel("Total Profit per Month USD") # Sets the y label to the total profit per month usd
    plt.show() # Shows the plot

    # Part B
    plt.bar(months, totalUnitsData) # Takes in months and totalUnitsData as the x and y for a bar graph
    plt.title("Total Units Sold vs. Months of year") # Sets the title to total units sold vs months of year
    plt.xlabel("Month of The Year") # Sets the x axis label to month of the year
    plt.ylabel("Total Units Sold per Month") # Sets the y axis label to total units sold per month
    plt.show() # Shows the bar graph



# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly