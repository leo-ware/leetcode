def fibonacci_iterative(n):
    """
    Finds the nth fibonacci number iteratively
    """
    
    # this dictionary will keep track of the numbers we have already calculated
    fibs = {0: 0, 1: 1}
    
    # we have to calculate every fibonnaci up to f(n)
    for i in range(2, n+1):
        
        # formula for f(i)
        fibs[i] = fibs[i-1] + fibs[i-2]
    
    # recover f(n) from the dictionary
    return fibs[n]


def fibonacci_recursive(n):
    """
    Finds the nth fibonacci recursively
    """
    
    # the two base cases
    if n in [0, 1]:
        return n
    
    # since the fibonacci sequence is itself defined recursively, all 
    # we have to do is write down the formula
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    

class MemoizedFib:
    """
    Class for finding the nth fibonacci with caching and recursion
    """
    
    def __init__(self):
        
        # old function calls are stored in a dictionary so lookups are O(1)
        self.cache = {1: 1, 0: 0}
    
    def __call__(self, arg, top_call=True):
        
        # check if we have stored this result
        try:
            ans = self.cache[arg]
            
        # if it's not found in the cache, compute the answer using the formula for fibonaccis and cache the result
        except KeyError:
            ans = self.__call__(arg-1, top_call=False) + self.__call__(arg-2, top_call=False)
            self.cache[arg] = ans
        
        # if this was the original call--and not one called inside the recursion--we reset state before returning
        # this means we don't need to reinstantiate every time to get accurate timing numbers
        if top_call:
            self.cache = {0:0, 1:1}
        
        return ans

# the way I defined the class this can now be treated as just another function
fibonacci_recursive_memoized = MemoizedFib()
