import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def extract_min(self):
        return heapq.heappop(self.heap)

# Test
min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(6)
min_heap.insert(5)
min_heap.insert(2)
min_heap.insert(4)

print(min_heap.extract_min())  # Output: 1
