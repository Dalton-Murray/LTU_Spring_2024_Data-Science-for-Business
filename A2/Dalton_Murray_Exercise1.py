#####################
## Dalton Murray    #
## 02/16/2024       #
## A2 - Exercise 1  #
#####################
import sys # Required for system functions

import numpy as np # Imports the numpy library and sets an alias to np
import statistics as stats # Imports the statistics library and sets an alias to sts

# Defines the __main__ function
def __main__():

    # Creates a variable called myList and sets the list data to the provided data
    myList = [24, 5, 15, 60, 54, 82, 99, 80, 70, 98, 93, 60, 33, 22, 65, 61, 51, 58, 83, 86, 42, 67, 60]

    ## Part 1
    # Calculates the mean of the list using numpy mean function then prints it out
    meanList = np.mean(myList)
    print("The mean is:", meanList)

    ## Part 2
    # Calculates the median of the list using numpy median function then prints it out
    medianList = np.median(myList)
    print("The median is:", medianList)

    ## Part 3
    # Mode calculation method 1
    # The assignment says we can use the numpy library but it doesn't say we cannot use other libraries, this would be the most simple way to calculate the mode
    # by using a preexisting library with a function already built in, however, we can do this with regular numpy and python alone shown in method 2
    modeList = stats.mode(myList)
    print("Method 1\nThe mode is:", modeList)

    # Mode calculation method 2
    # This method uses only numpy and uses in-line lambda with bins
    modeList = np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis = 0, arr = myList)
    print("Method 2\nThe mode is:", modeList)

    # Other methods of mode calculation
    # We did learn another method in class using a function with a counter and setting it to use the max function however,
    # I opted not to use this in order to expand upon/learning different and more ways to do it and I didn't want to just
    # take the method given to us and use it, similar with the other functions here, however, I didn't want to include
    # 3 different ways to do every function so I just used numpy instead for them where easiest to

    ## Part 4
    # Range calulcation method 1
    # This uses numpy to calculate the range of the list and then prints it out, however, this isn't a way we learned to do it, so I will include the other easy way too
    rangeList = np.ptp(myList)
    print("Method 1\nThe range is:", rangeList)

    # Range calculation method 2
    # This performs the range calculation using other calculation other than the built-in range calculator, this method was taught in class
    rangeList = np.max(myList, axis = 0) - np.min(myList, axis = 0)
    print("Method 2\nThe range is:", rangeList)

    ## Part 5
    # This calculates the variance using the numpy variance method and then prints it out (population variance not sample variance)
    varianceList = np.var(myList)
    print("The variance is:", varianceList)

    ## Part 6
    # This calculates the standard deviation using numpy functions (population not sample)
    standardDeviationList = np.std(myList)
    print("The standard deviance is:", standardDeviationList)

# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly