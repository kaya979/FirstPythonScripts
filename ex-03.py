a = input("enter your first name:")
b = input("enter your last name:")
c = input("enter your job title:")
d = input("enter your company name:")

thisdict = {
    "First Name:":a,
    "Last Name:":b,
    "Job Title:":c,
    "Company:":d,



}
print("-------------------------------------")
print(thisdict)
for key, value in thisdict.items():
    print(key,  ':',    value)
print("-------------------------------------")


#with open('GFG', 'w') as f:
      
    # using csv.writer method from CSV package
#    write = csv.writer(f)
      
#    write.writerow(fields)
#    write.writerows(rows)

#with open(..., 'w', newline='') as myfile:
 #    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(mylist

with open('test.csv', 'a') as f:
    f.write('key, value\n')
    for key in thisdict.keys():
        f.write("%s,%s\n"%(key,thisdict[key]))

        