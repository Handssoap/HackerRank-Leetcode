def checkMagazine(magazine, note):
    # this will hold all the words from the magazine and the number of times they appear
    mapMagazine = {}

    # fill the hashmap with the words from the magazine (case sensitive)
    for word in magazine:
       mapMagazine[word] = mapMagazine.get(word, 0) + 1


    # check if each word in the note is found in the magazine
    for word in note:
        if mapMagazine.get(word, 0) > 0:
            mapMagazine[word] -= 1
        else:
            # if not then print no
            print('No')
            return
    print('Yes')
    return