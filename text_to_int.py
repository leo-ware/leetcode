def text_to_int(string):
    """
    Maps a text description of a number to an integer, e.g. "two-thousand" --> 2000.
    """
    add = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'ninteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
    multiply = {'hundred': 100, 'thousand': 1000, 'million': 10**6, 'billion': 10**9, 'trillion': 10**12}
    
    answer = 0
    list_strings = [i.split('-') for i in string.split(' ')]

    for word in list_strings:
        temp = 0
        for mod in word:
            if mod in add.keys():
                temp += add[mod]
            elif mod in multiply.keys():
                temp *= multiply[mod]
            else:
                raise(ValueError(f"unknown word {mod}"))
        answer += temp
    
    return answer

assert(text_to_int('one')==1)
assert(text_to_int('one-hundred-thousand')==10**5)
assert(text_to_int('ten-million one-hundred-thousand fifteen')==10100015)
assert(text_to_int("ninety-nine-trillion fifty-five-thousand ten")==99*10**12+55*10**3+10)
