def double(oldlist):
    newlist=[]
    for i in oldlist:
        newlist.append(i*2)
    print(newlist)

string= input("Please enter your string : ")

oldlist=string.split(',')
oldlist=[int(i) for i in oldlist]
print("String after doubling all the numbers is : ",end="")
double(oldlist)