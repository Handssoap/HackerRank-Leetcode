def arrayManipulation(n, queries):
    
    # to avoid out of bounds issues
    arrToManipulate = [0] * (n + 2)

    
    for i in queries:
        # notate where we want to start adding
        prefix = i[0]
        # notate where we want to start subtracting
        suffix = i[1]
        # value to add/sub
        addition = i[2]
        # starting at this point,
        arrToManipulate[prefix-1] += addition
        arrToManipulate[suffix] -= addition
        
        current = 0
        max_value = 0
        
    for i in range(0, n):
        # keep track of the current indeces running sum
        current += arrToManipulate[i]
        if current > max_value:
            # this lets us know what our peak is in the array
            max_value = current
    return max_value
