# original kata on codewars https://www.codewars.com/kata/5877e7d568909e5ff90017e6/solutions/python

def find_all(sum_digs, num_digs, _min_size=1, _top_call=True):
    """
    We are interested in numbers whose digits sum to sum_digs, who have num_digs digits (no leading zeroes),
    and whose digits are in ascending (inclusive) order. This function returns a count of how many such 
    numbers exist, the minimum such number, and the maximum such number.
    """
    if num_digs == 1:
        if _min_size <= sum_digs < 10:
            return 1, str(sum_digs), str(sum_digs)
        else:
            return 0, str(sum_digs), str(sum_digs)
    
    ans_count = 0
    ans_first = False
    ans_last = "0"
    
    for num in range(_min_size, (sum_digs // num_digs)+1):
        count, first, last = find_all(sum_digs-num, num_digs-1, num, _top_call=False)
        ans_count += count
        
        if count:
            if not ans_first:
                ans_first = str(num) + str(first)
            ans_last = str(num) + str(last)
    
    if _top_call and ans_count == 0:
        return []
    
    return [ans_count, int(ans_first), int(ans_last)]
