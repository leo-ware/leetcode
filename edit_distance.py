def edit_distance(s1, s2):
    """
    Finds the minimum number of edits to make s1 and s2 equal. Uses
    dynamic programming.
    """
    
    # set up the cache
    # position (m, n) in the cache will contain the edit distance between
    # the string composed of the first m elements of s1 and the string composed
    # of the first n elements of s2
    cache = [[i+1 for i in range(len(s2))]] + [[0 for _ in s2] for range in s1]
    cache = [[i] + x for i, x in enumerate(cache)]
    
    # if you wanted, you could speed this up by using a hash map above
    
    for pos_1, char_1 in enumerate(s1):
        for pos_2, char_2 in enumerate(s2):
            
            # if they are the same, we can just do whatever we were doing before
            if char_1 == char_2:
                cache[pos_1+1][pos_2+1] = cache[pos_1][pos_2]
            
            # otherwise, we need to figure out whether to delete the last s1, the 
            # last s2, or edit them to be the same
            else:
                cache[pos_1 + 1][pos_2 + 1] = min(
                    cache[pos_1][pos_2],
                    cache[pos_1][pos_2 + 1],
                    cache[pos_1 + 1][pos_2]
                ) + 1
    
    return cache[-1][-1]

assert(edit_distance('foo', 'fo')==1)
assert(edit_distance('fofofo', 'foo')==3)
assert(edit_distance('', 'foo')==3)
assert(edit_distance('', '')==0)
