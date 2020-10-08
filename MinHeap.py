class MinHeapq:
    """ 
    This class implements properties and methods that support a min 
    priority queue data structure
    
    Attributes
    ----------
    heap : list
        A Python list where key values in the min heap are stored
        
    heap_size : int
        An integer counter of the number of keys present in the min heap
        
    """ 
    
    
    def __init__(self):
        """
        Class initialization method.
        
        Note
        ----
        Use heapq_var = MaxHeap()
        
        """
        self.heap       = []
        self.heap_size  = 0

        
    def mink(self):
        """
        This method returns the lowest key in the priority queue
        
        Note
        ----
        Use key_var = heap_var.max()
        
        """
        return self.heap[0] # which is the smallest element by the min-heap property
    
     
    def heappush(self, key):   
        """
        Inserts the value of key onto the priority queue, maintaining the
        min heap invariant.
        
        Note
        ----
        Use heapq_var.heappush(key)
        
        """
        self.heap.append(float("inf")) # new value must be smaller, so we start with the largest number
        self.decrease_key(self.heap_size,key) # shrinks inf down to the number we actually want and bubbles it up
        self.heap_size+=1 # increase heap size counter to account for new element
        
        
    def decrease_key(self, i, key): 
        """
        This method implements the DECREASE_KEY operation, which modifies 
        the value of a key in the min priority queue with a lower value. 
        
        Note
        ----
        Use heapq_var.decrease_key(i, new_key)
        
        """
        if key > self.heap[i]: # weird bugs are possible without this
            raise ValueError('new key is larger than the current key')
            
        self.heap[i] = key # assign the key to the specified index
        
        # keep swapping it with its parent until its parent is smaller than it
        while i > 0 and self.heap[parent(i)] > self.heap[i]:
            self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
            i = parent(i) 
            
        
    def heapify(self, i):
        """
        This method implements the MIN_HEAPIFY operation for the min priority
        queue. The input is the array index of the root node of the subtree to 
        be heapify.
        
        Note
        ----
        Use heapq_var.heapify(i)
        
        """
        
        # This is kind of garbage code. I would never write something with this many if statements.
        # That said, there isn't really an incentive to fix it.
        
        # give everything new names to maximize confusion
        l = left(i)
        r = right(i)
        heap = self.heap
        
        # figure out if the left or right child is smaller
        if l <= (self.heap_size-1) and heap[l] < heap[i]:
            smallest = l
        else:
            smallest = i
        if r <= (self.heap_size-1) and heap[r] < heap[smallest]:
            smallest = r
        
        # if one of them is smaller, swap and call this funcion recursively
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.heapify(smallest)


    def heappop(self):
        """
        This method implements the EXTRACT_MIN operation. It removes and returns the smallest
        key in the min priority queue.
        
        Note
        ----
        Use key_var = heapq_var.heappop() 
        
        """
        if self.heap_size < 1:
            raise ValueError('Heap underflow: There are no keys in the priority queue ')
        mink = self.heap[0] # we know this is the smallest element
        self.heap[0] = self.heap[-1] # put the last list element at the front
        self.heap.pop() # remove the last element from the list
        self.heap_size-=1 # shrink the size of the heap
        self.heapify(0) # bubble it down
        return mink


# testing

# generic test of all functionality
def test_1():
    A = MinHeapq()
    for i in [3, 2, 1]:
        A.heappush(i)
    assert(A.heap==[1, 3, 2])
    assert(A.mink()==1)
    
    assert(A.heappop()==1)
    assert(A.heap==[2, 3])
    
    A.decrease_key(1, 1)
    assert(A.heap==[1,2])

# make sure it can handle duplicates
def test_2():
    A = MinHeapq()
    for i in [2, 1, 1]:
        A.heappush(i)
    assert(A.mink()==1)
    assert(A.heap==[1, 2, 1])

# make sure it knows what to do with an empty list
def test_3():
    A = MinHeapq()
    try:
        A.heappop()
        assert(False)
    except ValueError:
        pass

# run all tests
test_1()
test_2()
test_3()
