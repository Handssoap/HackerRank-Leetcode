def minimumBribes(q):
    numberOfBribes = 0

    # loop through the list
    for i in range(0, len(q)):
        # the position of each int ..n, is -1 in the array
        original_pos = q[i] - 1

        # the diff is how many spots is the value away from its original position
        # ex: [2, 3, 1] 2 is 1 away, 3 is 1 away, 1 is - 2 away (meaning it was bribed twice) so we keep track of -
        diff = original_pos - i

        # a person can only be bribed twice, else return
        if diff > 2:
            print("Too chaotic")
            return
        # for the first two people in front of i (because that's the most based on previous if)
        for j in range(max(0, q[i] - 2), i):
            # check if the person in front of me, belongs behind me (did they bribe me)
            if q[j] > q[i]:
                numberOfBribes += 1

    print(numberOfBribes)