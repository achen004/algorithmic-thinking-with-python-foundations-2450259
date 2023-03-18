#Min number of coins needed to solve
#available UK coin denominations: 1p, 2p, 5p, 10p, 20p, 50p, 1pound, 2pound    

def change_make(value):
    counter=0
    coins=[]
    #choose the largest denom. to remove from value; multiple
    #make it all in digits
    denoms_1=[200, 100, 50, 20, 10, 5, 2, 1]
    for d in denoms_1:
        #check if value >= coin value
        while value>=d:
            value-=d
            coins.append(d)
            counter+=1
    return counter, coins

print(change_make(163))
