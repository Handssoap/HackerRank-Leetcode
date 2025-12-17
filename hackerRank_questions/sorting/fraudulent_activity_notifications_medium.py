def activityNotifications(expenditure, d):
    # we know expenditure is greater than 0 and lesss than 201, will keep track of how many times an arbitrary number appears in curr window
    # cannot use a hashmap as keys in a hashmap are not sorted
    count = [0] * 201

    for i in range(d):
        # int appears += 1 times, to keep track of frequency
        count[expenditure[i]] += 1

    # this is the hardest part of this question, we can't do sort each time, we have to figure out the median some other way,
    def getMedian():
        # acc will keep track of how many numbers weve seen so far
        acc = 0
        if d % 2 == 1:
            m = d // 2 + 1

            for i in range(201):
                # since count[i] stores the frequency a number appears, we can calculate the median by counting up to middle point of the window (d//2 + 1)
                acc += count[i]
                if acc >= m:
                    return i
        else:
            # the same logic is done here, but we have to keep track of two integers this time
            m1, m2 = d // 2, d // 2 + 1
            a = b = None
            for i in range(201):
                acc += count[i]
                if acc >= m1 and a is None:
                    a = i
                if acc >= m2:
                    b = i
                    break
            return (a + b) / 2

    notifications = 0

    for i in range(d, len(expenditure)):
        # simple calculatiosn from here
        median = getMedian()
        if expenditure[i] >= 2 * median:
            notifications += 1

        count[expenditure[i - d]] -= 1
        count[expenditure[i]] += 1

    return notifications

    # original implementation which was
    ''' 
    pointerStart = 0
        pointerEnd = d
        median = -99

        notifications = 0

        sublist = []

        for i in range(pointerEnd, len(expenditure)):
            #sort sub array
            if len(sublist) == 0:
                sublist = expenditure[pointerStart:pointerEnd]
                sublist.sort()
            else:
                sublist.pop(0)
                sublist = binaryInsert(expenditure[i-1], sublist)
            median = calculateMedian(sublist)
            if expenditure[i] >= median * 2:
                notifications+=1
            pointerStart+=1
            pointerEnd+=1

        return notifications

    def binaryInsert(n, arr):
        min1 = 0
        max1 = len(arr) - 1

        while True:
            mid = (min1 + max1) // 2
            if max1 - min1 == 1:
                arr.insert(mid + 1, n)
                break
            if n > arr[mid]:
                min1 = mid
            elif n < arr[mid]:
                max1 = mid
            elif n == arr[mid]:
                arr.insert(mid, n)
                break
        return arr
        # calculate median of range
    def calculateMedian(sortedList):
        print(sortedList)
        if len(sortedList) % 2 == 0:
            median =(sortedList[len(sortedList)//2] + sortedList[len(sortedList)//2 - 1]) / 2
        else: 
            median = sortedList[len(sortedList)//2] 
        return median
    '''