#####################
## Dalton Murray    #
## 01/31/2024       #
## A1 - Exercise 1  #
#####################
import sys # Required for system functions

import matplotlib as mplib # Imports matplotlib library and sets an alias to mplib
from matplotlib import pyplot as plt # Imports pyplot from matplotlib and sets an alias to plt

# Defines the __main__ function
def __main__():

    heightData= [143,144,141,141,141,145,149,147,152,154,152,151,154,153,
        154,150,153,154,156,158,159,158,159,155,158,157,158,159,
        159,158,158,159,156,156,157,156,159,155,157,162,160,160,
        164,160,164,160,163,163,163,164,163,164,162,162,163,161,
        160,163,162,162,164,164,160,161,163,166,166,168,166,168,
        167,167,167,168,168,168,165,169,167,166,166,169,166,168,
        168,168,169,168,166,168,165,169,167,169,167,168,167,165,
        169,168,165,167,167,165,166,165,166,165,167,165,168,165,
        166,169,168,169,167,167,170,173,173,172,171,174,174,174,
        173,172,172,174,171,174,173,173,170,172,174,171,172,174,
        170,170,174,174,170,170,174,173,171,174,170,170,170,174,
        170,173,170,174,173,171,173,171,170,174,171,174,172,173,
        170,172,173,174,170,171,170,170,172,173,172,171,174,172,
        171,179,178,179,179,176,175,175,176,177,177,177,177,179,
        178,178,178,175,175, 183,184,182,182,184,183,180,182,180,
        182,180,183,182,180,180,184,181,181,180,182,180,187,189,188] # Defines the variable heightData and creates a list with the already given data

    plt.hist(heightData, bins = 5) # Create a histogram out of the variable heightData's data and sets bin sizes to 5
    plt.xlabel("Height in CM") # Sets the x axis label
    plt.ylabel("Number of persons") # Sets the y axis label
    plt.title("Histogram for Height Distribution") # Sets the title of the plot
    plt.show() # Shows the plot



# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly