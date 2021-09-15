#Loops
#Introduction:
#You can use loops when you want to run a block of code multiple times. 
# For example, you might want to do an operation on every item in a (large) list, 
# or you want to write an algorithm that follows the same set of instructions 
# for multiple iterations.
#There are two types of loops in Python: the while loop and the for loop.
#The while loop runs while a condition is true. 
# They can run indefinitely if that condition never changes. 
# If your code is stuck in an infinite loop, just press ctrl-c (or command-c on MacOS) 
# to force quit the running code.
# The for loop runs for a predetermined number of iterations. 
# This number can be hard coded using the range() function, 
# or dynamically assigned (using a variable, the size of a list, 
# or the number of lines in a document). 
# It is also possible to accidentally create an infinite for-loop. 
# You can use the same command (ctrl/cmd+c) to exit your program.

x = 0
while x <= 10:
    print(x)
    x +=1

#The while loop runs while a condition is true. They can run indefinitely if that condition never changes. 
# If your code is stuck in an infinite loop, just press ctrl-c (or command-c on MacOS) to force quit the running code.

