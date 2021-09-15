getallen = [12, 23, 5, 3, 8]

print("Mijn getallen", getallen)

lengte = len(getallen)
teller = 0 

for getal in getallen[1:]:
    getal1 = getal +getallen[teller]
    teller = teller +1 
    print(getal1)
    if teller == lengte -1:
        getal1 = getal + getallen[0]
        