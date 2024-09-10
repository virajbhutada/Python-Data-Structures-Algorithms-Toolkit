from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def is_empty(self):
        return not self.q1

# Test
stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())  # Output: 3
stack.pop()
print(stack.top())  # Output: 2
