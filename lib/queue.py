'''
Characteristics:
    - FIFO (First In First Out)
    - Can be implemented with LinkedList/Array

Runtime Complexity:
- All operations: O(1)
'''


class ArrayQueue:
    # [10, 20, 30, 0, 0]
    #  f        r
    CAPACITY = 5

    def __init__(self):
        self.items = [0 for _ in range(ArrayQueue.CAPACITY)]
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        if self.rear == ArrayQueue.CAPACITY:
            raise Exception("Queue is full")

        self.items[self.rear] = item
        self.rear += 1

    def dequeue(self):
        if self.front == ArrayQueue.CAPACITY:
            raise Exception("Queue is empty")
        self.front += 1
        return self.items[self.front - 1]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear - self.front) == ArrayQueue.CAPACITY
