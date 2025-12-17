def maximumToys(prices, k):
    #sort prices
    prices.sort()
    numberOfToys = 0
    # since we're looking for max number of toys, sum the first few
    for n in prices:
        if k - n >= 0:
            k -= n
            numberOfToys+=1
        else:
            return numberOfToys