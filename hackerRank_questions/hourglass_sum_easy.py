def hourglassSum(arr):
    # running sum problem

    # - 63 is the minimum sum -9 x 7 values
    maximum_sum = -63
    for i in range(4):
        for j in range(4):
            # basically since we know the hourglass shape and there's 4 per row, we have to do 16 loops to calculate the sum of each hourglass, 4 hourglasses per row and 4 per column
            current_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            current_sum += arr[i + 1][j + 1]
            current_sum += arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if current_sum > maximum_sum:
                maximum_sum = current_sum
    return maximum_sum