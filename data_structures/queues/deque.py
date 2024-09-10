class Deque:
    def __init__(self, size):
        self.size = size
        self.deque = [None] * size
        self.front = -1
        self.rear = 0

    def insert_front(self, data):
        if (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1):
            print("Deque is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.deque[self.front] = data
        elif self.front == 0:
            self.front = self.size - 1
            self.deque[self.front] = data
        else:
            self.front -= 1
            self.deque[self.front] = data

    def insert_rear(self, data):
        if (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1):
            print("Deque is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.deque[self.rear] = data
        elif self.rear == self.size - 1:
            self.rear = 0
            self.deque[self.rear] = data
        else:
            self.rear += 1
            self.deque[self.rear] = data

    def delete_front(self):
        if self.front == -1:
            print("Deque is empty")
        else:
            temp = self.deque[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            elif self.front == self.size - 1:
                self.front = 0
            else:
                self.front += 1
            return temp

    def delete_rear(self):
        if self.front == -1:
            print("Deque is empty")
        else:
            temp = self.deque[self.rear]
            if self.front == self.rear:
                self.front = self.rear = -1
            elif self.rear == 0:
                self.rear = self.size - 1
            else:
                self.rear -= 1
            return temp

    def display(self):
        if self.front == -1:
            print("Deque is empty")
        else:
            print("Deque elements:", end=" ")
            if self.rear >= self.front:
                for i in range(self.front, self.rear + 1):
                    print(self.deque[i], end=" ")
            else:
                for i in range(self.front, self.size):
                    print(self.deque[i], end=" ")
                for i in range(0, self.rear + 1):
                    print(self.deque[i], end=" ")
            print()
