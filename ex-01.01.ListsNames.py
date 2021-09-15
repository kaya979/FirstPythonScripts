#Lists
#You can declare a list of values in a single variable. 
# A list is represented by square brackets [], and each value is separated by a comma.

#Each position in a list has a number associated with it called the index. 
# Indexes start at 0, so the first item in a list will have the index 0. 
# The second item will have index 1, etc. 
# You can call individual items in a list by calling its index.

#You can loop over a list using a for loop. 
# Instead of a number within a range, i 
# (or whatever you name the variable you declare) 
# will have the value of an item in the list. 
# You can still use range() to loop over a list. 
# In this case, i will be used to call an index in a list.


#Exercise 1:
#Create a new script.
#Create a variable that contains a list of five names.
#Loop over the list using a for loop. Print every individual name in the list on a new line.
#Example output:
#Casper
#Coen
#Kim Sing
#Achraf
#Clyde

#[index 0, index 1, index 2, index 3,...]  this is an index, the first position is index 0
#[0,1,2,3,4,5,6] # an index always starts at the bracket[ then zero, then 1, etc,...and ends with last bracket]
#[23,12,14,54,65,43] #now 23 is index zero, 12 is index 1


names = ["Achraf", "Antonio", "Kaya", "Sameer"]
for x in names:
    print(x)

    