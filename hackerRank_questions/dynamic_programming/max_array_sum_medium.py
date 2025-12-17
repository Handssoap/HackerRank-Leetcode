def maxSubsetSum(arr):
    prev2 = 0
    prev1 = 0

    for i in arr:
        # when looking at the current value, we have two choices:
        # skip or take, if we take then we can't take the previous value
        # if all values are negative then we default to 0
        current = max(prev1, prev2 + i, 0)
        prev2 = prev1
        prev1 = current

    return prev1