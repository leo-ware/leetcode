def spiralize(size):
    """
    Creates a size x size array of zeroes with ones inserted in the shape of a clockwise spiral.
    """

    if size == 0:
        return []

    spiral = [[0 for _ in range(size)] for _ in range(size)]
    position = [0, 0]

    def move_right(): position[0] += 1
    def move_left(): position[0] -= 1
    def move_up(): position[1] -= 1
    def move_down(): position[1] += 1
    def punch(): spiral[position[1]][position[0]] = 1
    
    # punch the top row
    punch()
    for _ in range(size-1):
        move_right()
        punch()
    
    # we will alternate through directions
    moves = [move_right, move_down, move_left, move_up]

    span = size-1 # number of punches to make
    move = 1 # which direction to go

    while span > 0:
        for _ in range(2):
            for _ in range(span):
                moves[move]()
                punch()
            if span==1: break # we don't want it curling back in on itself
            move = (move+1)%4
        span -= 2

    return spiral


# test cases

sp_0 = []

sp_2 = [
        [1, 1],
        [0, 1]
        ]

sp_5 = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
        ]

sp_8 = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
        ]

assert(spiralize(0)==sp_0)
assert(spiralize(2)==sp_2)
assert(spiralize(5)==sp_5)
assert(spiralize(8)==sp_8)
