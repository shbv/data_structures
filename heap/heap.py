"""
Heaps: Binary trees with 2 properties
   - Complete binary tree: All levels full, except may be last (filled from left to right)
   - Heap order property: Nodes are ordered  (not sorted)
        - Max heap: key(parent) >= key(child). root node had max element of heap
        - Min heap: key(parent) <= key(child). root node has min element of heap

Usage:
    - Priority queues (get min/max in O(1)) 

Representation:
    - Python list/array (space-efficient)
        - parent index = k
            - left-child index = 2k+1, right-child index = 2k+2
        - child index = i
            - parent index = (i-1)//2 
        - last index = n-1
            - last parent = (n-2)//2)  (at middle of array/list)
    - Node & Tree classes

Operations: 
    - get_max/min(): O(1)
        - return root-node
    - build max/min heap: O(n)
        - Start from last index or last parent (index: (n-2)//2)
        - bottom-up (percolate down / max/min heapify): 3-way compare node & its children, & swap  
    - extract max: O(logn)
        - replace root node with last child node
        - top-down (percolate down / max/min heapify): 3-way compare node & its children, & swap 
    - Insert: O(logn)
        - insert at leaf 
        - bottom-up (percolate up): compare node & its parent, & swap 
"""

class MyMaxHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def get_max(self):
        if len(self.heap) > 0: 
            return self.heap[0]
        else:
            return None

    def __max_heapify(self, index):
        """ fix heap order topdown from node to leaf: 
            3-way compare node & its children, & swap, and recurse downward """
        left_ix = 2*index + 1
        right_ix = 2*index + 2
        largest_ix = index
        if left_ix < len(self.heap) and self.heap[left_ix] > self.heap[largest_ix]:
            largest_ix = left_ix
        if right_ix < len(self.heap) and self.heap[right_ix] > self.heap[largest_ix]:
            largest_ix = right_ix
        if largest_ix != index:
            #swap largest & index
            self.heap[index], self.heap[largest_ix] = self.heap[largest_ix], self.heap[index]
            self.__max_heapify(largest_ix)

    def build_heap(self, lst):
        """ bottom-up max_heapify each node from last parent to root node """
        self.heap = lst
        last_parent_ix = (len(self.heap)-2)//2 
        for ix in range(last_parent_ix, -1, -1):
            self.__max_heapify(ix)

    def extract_max(self):
        """ remove root node, swap last node & root node, and max_heapify root node"""
        if len(self.heap) == 1:
            max_value = self.heap[0]
            del self.heap[0]
            return max_value
        elif len(self.heap) > 1:
            max_value = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__max_heapify(0)
            return max_value
        else:
            return None
            
    def __percolate_up(self, index):
        """ compare node & its parent, and swap, and recurse upward """
        if index <= 0:  # base case of recursion, reached root node
            return 
        parent_ix = (index-1)//2
        if self.heap[index] > self.heap[parent_ix]:
            self.heap[parent_ix], self.heap[index] = self.heap[index], self.heap[parent_ix]
            self.__percolate_up(parent_ix)
    
    def insert(self, value):
        self.heap.append(value) # O(1) amortized time in python
        index = len(self.heap)-1
        self.__percolate_up(index) # find its correct spot

    def print_preorder(self, index=0):
        if index < len(self.heap):
            print(self.heap[index])
            self.print_preorder(2*index+1) # left child
            self.print_preorder(2*index+2) # right child

class MyMinHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def get_min(self):
        if len(self.heap) > 0: 
            return self.heap[0]
        else:
            return None

    def __min_heapify(self, index):
        """ fix heap order topdown from node to leaf: 
            3-way compare node & its children, & swap, and recurse downward """
        left_ix = 2*index + 1
        right_ix = 2*index + 2
        smallest_ix = index
        if left_ix < len(self.heap) and self.heap[left_ix] < self.heap[smallest_ix]:
            smallest_ix = left_ix
        if right_ix < len(self.heap) and self.heap[right_ix] < self.heap[smallest_ix]:
            smallest_ix = right_ix
        if smallest_ix != index:
            #swap smallest & index
            self.heap[index], self.heap[smallest_ix] = self.heap[smallest_ix], self.heap[index]
            self.__min_heapify(smallest_ix)

    def build_heap(self, lst):
        """ bottom-up min_heapify each node from last parent to root node """
        self.heap = lst
        last_parent_ix = (len(self.heap)-2)//2 
        for ix in range(last_parent_ix, -1, -1):
            self.__min_heapify(ix)

    def extract_min(self):
        """ remove root node, swap last node & root node, and min_heapify root node"""
        if len(self.heap) == 1:
            min_value = self.heap[0]
            del self.heap[0]
            return min_value
        elif len(self.heap) > 1:
            min_value = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__min_heapify(0)
            return min_value
        else:
            return None
            
    def __percolate_up(self, index):
        """ compare node & its parent, and swap, and recurse upward """
        if index <= 0:  # base case of recursion, reached root node
            return 
        parent_ix = (index-1)//2
        if self.heap[index] < self.heap[parent_ix]:
            self.heap[parent_ix], self.heap[index] = self.heap[index], self.heap[parent_ix]
            self.__percolate_up(parent_ix)
    
    def insert(self, value):
        self.heap.append(value) # O(1) amortized time in python
        index = len(self.heap)-1
        self.__percolate_up(index) # find its correct spot

    def print_preorder(self, index=0):
        if index < len(self.heap):
            print(self.heap[index])
            self.print_preorder(2*index+1) # left child
            self.print_preorder(2*index+2) # right child


if __name__ == "__main__":

    # Max heap

    print(f"\n== Max heap ==\n")
    heap = MyMaxHeap()
    lst = [10, 30, 50, 70, 5]

    print(f"== Inserting {lst} into heap one at a time ==")
    for val in lst:
        heap.insert(val)
    print(f"heap: {heap}")
    print("Print preorder:")
    heap.print_preorder()
    print(f"max: {heap.get_max()}")

    print(f"== Build heap from list {lst} ==")
    heap.build_heap(lst)
    print(f"heap: {heap}")
    print("Print preorder:")
    heap.print_preorder()
    print(f"max: {heap.get_max()}")

    print(f"== Extract max: {heap.extract_max()} ==")
    print("Print preorder:")
    heap.print_preorder()
    print(f"new max: {heap.get_max()}")

    # Min heap

    print(f"\n== Min heap ==\n")
    heap = MyMinHeap()
    lst = [70, 50, 30, 10, 5]

    print(f"== Inserting {lst} into heap one at a time ==")
    for val in lst:
        heap.insert(val)
    print(f"heap: {heap}")
    print("Print preorder:")
    heap.print_preorder()
    print(f"min: {heap.get_min()}")

    print(f"== Build heap from list {lst} ==")
    heap.build_heap(lst)
    print(f"heap: {heap}")
    print("Print preorder:")
    heap.print_preorder()
    print(f"min: {heap.get_min()}")

    print(f"== Extract min: {heap.extract_min()} ==")
    print("Print preorder:")
    heap.print_preorder()
    print(f"new min: {heap.get_min()}")
    


