def rotLeft(a, d):
    # ok we're not actually 'rotating' we just calculate where all the values should be after d rotations
    n = len(a)
    # we only need to know the amount of rotations before the array is the same again, so we get mod
    d %= n
    # splits the array into two, left side contains the ints which are d away from the start
    # right side is the ints up to d
    # kinda unintuitive at first
    result = a[d:] + a[:d]
    return result
