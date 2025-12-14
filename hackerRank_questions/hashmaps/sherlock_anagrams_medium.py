def sherlockAndAnagrams(s):
    # store count of all substrings
    substr_count = {}
    # for a string of length n, there are n(n+1)/2 substrings
    n = len(s)

    # generate all substrings
    # i chooses every possible starting position for a substring
    for i in range(n):
        # i is the starting index, j is the ending index + 1 because [i:j] excludes j

        # j chooses every possible ending position starting from i,
        # smallest valid susbtring is 1 character so i+1
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            # Sort the substring so that all anagrams map to the same key
            key = ''.join(sorted(substring))
            substr_count[key] = substr_count.get(key, 0) + 1

    total_pairs = 0
    for count in substr_count.values():
        # calculate the number of combinations of substrings
        total_pairs += count * (count - 1) // 2
    return total_pairs