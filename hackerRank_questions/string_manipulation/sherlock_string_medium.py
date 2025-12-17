def isValid(s):
    # map for all character frequencies
    charMap = {}
    for char in s:
        charMap[char] = charMap.get(char, 0) + 1
    numberOfTimesSubtracted = 0

    # find the mode; what is the mode of frequency of characters of strings
    counts = {}
    for x in charMap.values():
        counts[x] = counts.get(x, 0) + 1
    mode = max(counts, key=counts.get)

    # given the mode, we can compare how many times each character occurs in the string with the mode
    for val in charMap.values():
        if val == mode:
            continue
            # if the frequency != mode, and is 1, then we can remove the character altogether
        if val == 1:
            numberOfTimesSubtracted += 1
            # if frequency != mode, and is 1 greater than mode, subtract it by 1
        elif val - 1 == mode:
            numberOfTimesSubtracted += 1
        else:
            return 'NO'
    return 'YES' if numberOfTimesSubtracted <= 1 else 'NO'