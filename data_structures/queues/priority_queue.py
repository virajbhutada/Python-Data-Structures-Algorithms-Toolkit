import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        heapq.heappush(self.queue, data)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            return heapq.heappop(self.queue)

    def display(self):
        print("Priority Queue:", self.queue)
