def find_anagrams(word, candidates):
    for i in candidates:
        count1 = 0
        # print(i)
        candsp = list(i)
        # print(candsp)
        for j in word:
            # print(j)
            if j in candsp:
                candsp.remove(j)
                # print(candsp)
                count1 += 1
            else:
                #print("continue")
                break
        if len(word) == count1:
            return(print(i))
    return(print("No matches"))
    
find_anagrams(word, candidates)