#Exercise 3:
#Create a new script.
#Copy the code below into your script.

#Then Write the custom function avg() so that it returns the average of the given parameters.


def avg(x,y):
    #write your code here 
    #sum = [x, y]
    #avg = statistics.mean(sum)
    #return avg
    avg = (x + y)/ 2
    return avg

 
x = 128
y = 255
z = avg(x,y)
# print ("The average of",x,"and", y, "is", z)

avg(x,y)