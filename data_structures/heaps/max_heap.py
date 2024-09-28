import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, -val)

    def extract_max(self):
        return -heapq.heappop(self.heap)

# Test
max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(1)
max_heap.insert(6)
max_heap.insert(5)
max_heap.insert(2)
max_heap.insert(4)

print(max_heap.extract_max())  # Output: 6
