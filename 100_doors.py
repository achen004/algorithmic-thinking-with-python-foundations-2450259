#100 doors initially closed
#door closed, open; door open, close
#visit every door; next iteration, every 2nd door.. etc.
#which doors are open after the last pass?

#False: Close; True: Open
doors=[False]*101

#print(doors)

i=1
tds=len(doors)
while i<tds:
    #select new door variable from original iterative list
    for j in range(i, tds, i):
        doors[j]=not doors[j] #switches the boolean
    i+=1

for i in range(1, tds):
    if doors[i]==True:
        print(i, doors[i])



