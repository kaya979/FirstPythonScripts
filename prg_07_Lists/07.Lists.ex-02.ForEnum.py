#Exercise 2:
#Create a new script.
#Create a list of five integers.
#Use a for loop to do the following for every item in the list:
#Print the value of that item added to the value of the next item in the list. 
# #If it is the last item, add it to the value of the first item instead 
# (since there is no next item).




#mylist = [2,4,4,5,3]
#for x in mylist:
#    print(x)

a = [2,4,4,5,3]
for i, e in enumerate(a):
    if(i<(len(a)-1)):
        print(e + a[i+1])
    else: 
        print(a[0] + a[i])





