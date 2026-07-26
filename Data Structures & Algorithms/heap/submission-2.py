class MinHeap:

    def _swap(self, index_a, index_b):
        tmp = self.data[index_a]
        self.data[index_a] = self.data[index_b]
        self.data[index_b] = tmp 
    
    def _bubble_up(self, index):
        while index > 0:
            parent_index = math.floor((index - 1) / 2)

            if self.data[index] < self.data[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _bubble_down(self, index):
        last_index = len(self.data) - 1

        while True:
            left_child = (2 * index) + 1
            right_child = (2 * index) + 2
            smallest = index
            
            if left_child <= last_index and self.data[left_child] < self.data[smallest]:
                smallest = left_child
            
            if right_child <= last_index and self.data[right_child] < self.data[smallest]:
                smallest = right_child

            if smallest == index:
                break
            
            self._swap(index, smallest)
            index = smallest

    def __init__(self):
        self.data  = list() 

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.data) > 1:
            last_index = len(self.data) - 1
            self._bubble_up(last_index)


    def pop(self) -> int:
        if len(self.data) == 0:
            return -1 
        
        min_value = self.data[0]
        
        if len(self.data) == 1:
            self.data = list()
            return min_value

        last_element = self.data.pop()

        self.data[0] = last_element

        self._bubble_down(0)

        return min_value


    def top(self) -> int:
        if len(self.data) == 0:
            return -1
        return self.data[0]
        

    def heapify(self, nums: List[int]) -> None:
        self.data = nums[:] # Make a copy of the list
        last_parent = (len(self.data) - 2) // 2
        
        # Loop backwards from the last parent down to 0
        for i in range(last_parent, -1, -1):
            self._bubble_down(i)
        