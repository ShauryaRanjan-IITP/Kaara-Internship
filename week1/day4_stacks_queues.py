class stack :

    def __init__(self) :
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.is_empty(): 
            return self.stack.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        return print(self.stack())

#queue
from collections import deque

class Queue:

    def __init__(self):
        self.q = deque()

    def enqueue(self, val):
        self.q.append(val)

    def dequeue(self):

        if not self.empty():
            return self.q.popleft()

    def front(self):

        if not self.empty():
            return self.q[0]

    def empty(self):
        return len(self.q) == 0
