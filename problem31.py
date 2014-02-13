coins = [1,2,5,10,20,50,100,200]

cache = {}

def howManyWays(amount,coinList):
    ways = 0
    if (amount == 0):
        return 1
    
    for x in filter(lambda y: y <= amount, coinList):
        if (amount - x, x) in cache.keys():
            ways = ways + cache[(amount-x,x)]
        else:
            cache[(amount-x,x)] = howManyWays(amount - x, filter(lambda y: y <= x, coinList))
            ways = ways + cache[(amount-x,x)]
            
    return ways

