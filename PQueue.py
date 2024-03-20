# Implements a priority queue with the min-heap datatype.
class PQueue:
    def __init__(self):
        self.heap = []

    def push(self, point):
        self.heap.append(point)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_point = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_point
        
    def _heapify_up(self, position):
        while position > 0:
            parent_position = (position - 1) // 2
            if self.heap[position].f < self.heap[parent_position].f:
                self.heap[position], self.heap[parent_position] = self.heap[parent_position], self.heap[position]
                position = parent_position
            else:
                break
        
    def _heapify_down(self, position):
        left_child = 2*position + 1
        right_child = 2*position + 2
        smallest_position = position
        if left_child < len(self.heap) and self.heap[left_child].f < self.heap[smallest_position].f:
            smallest_position = left_child

        if right_child < len(self.heap) and self.heap[right_child].f < self.heap[smallest_position].f:
            smallest_position = right_child

        if smallest_position != position:
            self.heap[position], self.heap[smallest_position] = self.heap[smallest_position], self.heap[position]
            self._heapify_down(smallest_position) 

    def print_queue(self):
        print(self.heap)

