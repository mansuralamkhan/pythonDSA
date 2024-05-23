class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return (i -1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, priority, item):
        self.heap.append(priority, item)
        self.size += 1
        self.heapify_up(self.size -1)

    def pop(self):
        if self.size == 0:
            return None
        
        top_item = self.heap[0][1]
        self.heap[0] = self.heap[self.size - 1]
        del self.heap[self.size -1]
        self.size -= 1
        self.heapify_down(0)
        return top_item
    

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
            self.swap(i, )
            