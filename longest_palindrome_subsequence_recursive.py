class LongestPalindromeSubsequence:
    """
    Class for finding the lonest palindrome subsequence of a list.
    
    Cache is maintained beween calls. Do not reuse.
    """

    def __init__(self):
        self.actual_cache = {}
    
    def cache(self, start, stop, value=None):
        # handles get and set for the cache
        if value is not None:
            self.actual_cache[f"{start},{stop}"] = value
            return value
        else:
            return self.actual_cache[f"{start},{stop}"]
    
    def get_lps(self, string, _start=None, _stop=None):
        """
        Finds the longest palindrome subsequence of a string, e.g. ABA --> 3.
        """
        # only used in the top call
        if _start is None:
            _start = 0
        if _stop is None:
            _stop = len(string)-1 # inclusive endpoint

        # base case
        if _start >= _stop:
            return int(_start == _stop)
        
        # memoized case
        try:
            return self.cache(_start, _stop)
        except KeyError:
            pass
        
        # front/back same case
        if string[_start] == string[_stop]:
            return self.cache(_start, _stop, 2 + self.get_lps(string, _start + 1, _stop - 1))
        
        # front back different case
        return self.cache(_start, _stop, max(
            self.get_lps(string, _start + 1, _stop),
            self.get_lps(string, _start, _stop - 1)
            ))


# tests

test_cases = {
    "ABA": 3,
    "": 0,
    "A": 1,
    "ABADDA": 4,
    "amanaplanacanalpanama": 21
}

for string in test_cases:
    assert(LongestPalindromeSubsequence().get_lps(string)==test_cases[string])
