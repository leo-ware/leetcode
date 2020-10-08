class LeastCommonSubsequence():
    """
    Class for finding the longest common subsequence of two strings using a recursive/dynamic programming approach.

    Based on https://youtu.be/Qf5R-uYQRPk
    """

    def __init__(self):
        self.cache = {}
    
    def cache_ans(self, ans, n, r):
        self.cache[f"{n},{r}"] = ans
        return ans

    def get_lcs(self, P, Q, n=None, r=None):
        """
        Finds the longest common subsequence of strings P[:n+1] and Q[:r+1] recursively.
        """
        if n is None:
            n = len(P)-1
        if r is None:
            r = len(Q)-1

        # base case
        if -1 in [n, r]:
            return 0
        
        # memoized case
        try:
            return self.cache[f"{n},{r}"]
        except KeyError:
            pass
        
        # last character matching case
        if P[n] == Q[r]:
            return self.cache_ans(1 + self.get_lcs(P, Q, n=n-1, r=r-1), n=n, r=r)
        
        # last character nonmatching case
        return self.cache_ans(max(self.get_lcs(P, Q, n=n-1, r=r), self.get_lcs(P, Q, n=n, r=r-1)), n=n, r=r)

assert(LeastCommonSubsequence().get_lcs("ABC", "ABE")==2)
assert(LeastCommonSubsequence().get_lcs("", "ABE")==0)
assert(LeastCommonSubsequence().get_lcs("ABCEEFDEG", "ABEEHG")==5)
assert(LeastCommonSubsequence().get_lcs("ABCEEF", "ABE")==3)
