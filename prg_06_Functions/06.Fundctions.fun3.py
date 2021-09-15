def avg(x,y,s):
    #write your code here 
    #sum = [x, y]
    #avg = statistics.mean(sum)
    #return avg
    avg = (x + y +s)/ 3
    return avg

 
x = 100
y = 150
s = 50
z = avg(x,y,s)
print ("The average of",x,"and", y, "and", s, "is", z)