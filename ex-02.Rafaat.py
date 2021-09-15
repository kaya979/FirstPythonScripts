number = [2,4,4,5,3]

#for i in range(10):

for i in range(len(number)):
        try:
            print(number[i]+number[i+1])
        except:
            print(number[-1]+number[0])       #[-1] betekent de laatste cijfer, [0] optellen bij index 0
            

#len(numbers)            #len telt het aantal values, hoeveel waardes zijn er, nu 5 dus
    
