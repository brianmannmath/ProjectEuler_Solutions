coins = [1,2,5,10,20,50,100,200]



def howManyWays(amount,coinList):
    ways = 0

    if (amount == 0):
        return 1
    
    for x in filter(lambda y: y <= amount, coinList):
        ways = ways + howManyWays(amount - x, filter(lambda y: y <= x, coinList))

    return ways


print howManyWays(200, coins)
