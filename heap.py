class Heap:
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        #comparison function
        self.comparison_function = comparison_function  
        self.heap = list(init_array)
        #calling self.build to form the hap from the array as array might not be in from of arranged heap
        self.build_heap()

    
    def build_heap(self):
     # Start from the last non-leaf node and heapify down to the root   
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def size(self):
        #returns number of elements in heap
        return len(self.heap)
    
    def heapify_down(self, index):
        #heapify down the elemnet at given index
        size = len(self.heap)
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
         # Compare with left child
        if left < size and self.comparison_function(self.heap[left], self.heap[smallest]):
            smallest = left
        
        # Compare with right child
        if right < size and self.comparison_function(self.heap[right], self.heap[smallest]):
            smallest = right
        
        # If the smallest is not the current index, swap and continue heapifying down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)
    
    def heapify_up(self, index):
       
        #heapify the element up at a given index
        parent = (index - 1) // 2
         # If the current element is smaller than its parent, swap them
        if index > 0 and self.comparison_function(self.heap[index], self.heap[parent]):
            # Swap the current element with its parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            # Heapify up recursively
            self.heapify_up(parent)
    
    def insert(self, value):
        
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        #add the value at last of heap 
        self.heap.append(value)
        #shift the elemnt up to maintain the minimum property
        self.heapify_up(len(self.heap) - 1)
        
    
    def extract(self):
        
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        #heap is empty
        if len(self.heap) == 0:
            return None 
        
        # the minimum element
        root = self.heap[0]
        
     #move element to last to remove it 
        self.heap[0] = self.heap[-1]
        self.heap.pop()  
        
        # Heapify down to maintain the heap
        self.heapify_down(0)
        
        return root
    
    def top(self):
        
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        #empty heap
        if len(self.heap) == 0:
            return None  
        
        return self.heap[0]
    
   
    def is_empty(self):
        return len(self.heap) == 0
    
    def print(self):
        print(self.heap)