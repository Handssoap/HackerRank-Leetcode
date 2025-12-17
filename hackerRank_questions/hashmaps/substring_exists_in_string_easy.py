def twoStrings(s1, s2):
    #empty map to hold all chars of one of hte strings
    charMap = {}
    #store all chars of string 1
    for char in s1:
        charMap[char] = charMap.get(char, 0) + 1
    #see if any char in s2 is in s1
    for char in s2:
        if charMap.get(char, 0) > 0:
            return 'YES'
    return 'NO'