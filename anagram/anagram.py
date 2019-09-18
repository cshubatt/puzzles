def find_anagrams(word, candidates):
    wordsp = word.split()
    for i in candidates:
        test_wordsp = i.split()
        for j in wordsp:
            if j in test_wordsp:
                test_wordsp.remove(j)
            else:
                break
        return(print(i))
    return(print("No matches"))
    
find_anagrams()