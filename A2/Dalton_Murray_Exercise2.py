#####################
## Dalton Murray    #
## 02/16/2024       #
## A2 - Exercise 2  #
#####################
import sys # Required for system functions

# Defines the __main__ function
def __main__():

    ## Part 1 - A
    # Using with allows for the automatic handling of the file better/closing the file rather than typing additional code to close it
    # What this does is opens the file in read mode and sets it to the variance file, it then reads everything in the file and sets it
    # to the variable contents and then prints it out, since I am using with I do not have to worry about using file.close()
    with open("./Sample.txt", "r") as file:
        contents = file.read()
        print("Method 1\n", contents)

    # Another method of reading the contents without using with
    file = open("./Sample.txt", "r")
    contents = file.read()
    print("Method 2\n", contents)
    file.close()

    ## Part 1 - B
    # Rather than including the appending to the first part, I will include the first part but in appending mode just to show that I know
    # how to do both read only and appending modes, I will also only do this using with
    with open("./Sample.txt", "a") as file:
        file.write("This is my second assignment!\n")
    with open("./Sample.txt", "r") as file:
        contents = file.read()
        print("Appended file\n", contents)

    # Although the above method is efficient, it has additional unnecessary lines because it has to open it in appending mode then close then put it in reading then close again
    # This is where different modes come into play to be more efficient
    # The mode a+ stands for appending mode plus read operations
    with open("./Sample.txt", "a+") as file:
        file.write("This is my second assignment!")
        # Appending mode opens the file at the bottom/end of the position and then writes to it, because of this I then have to change the position I read from in order
        # to actually get the contents of the whole file
        file.seek(0)
        contents = file.read()
        print("Appended file\n", contents)
        # This does make for a weird file with the two written things, the first one when opening in only append mode, on the same line, this is because I'm  not telling it to go to
        # the next line yet, which would be done by adding \n at the first write statement which I have included now even though in the instructions it doesn't say to do so, in order to make
        # my program run and look better


    ## Part 2
    # This creates a new file called myfile.txt if it does not exist, it then puts into write+ mode so I can perform both writing and reading of the file at the same time to make sure everytime I run,
    # the file doesn't keep infinitely expanding like a+ mode, where I then create a first row having the columns of the file
    # I then perform another write with the contents for the first row, also using tabs for spacing, I then go back to the top of the file and read and print it out
    with open("myfile.txt", "w+") as file:
        file.write("firstName\tlastName\tclassNumber\tclassName\tassigntmentNumber\n")
        file.write("Dalton\tMurray\tINT7623\tData Science for Business\t02")
        file.seek(0)
        contents = file.read()
        print("New file\n", contents)



# Checks if the "__name__" variable equals "__main__"
if __name__ == "__main__":
    sys.exit(__main__()) # Calls the "__main__" function and then after running exits smoothly