'''
Characteristics:
    - FIFO (First In First Out)
    - Can be implemented with LinkedList/Array

Runtime Complexity:
- All operations: O(1)
'''
from queue import Queue


class ArrayQueue(Queue):
    def __init__(self):
        self.items = [0 for _ in range(Queue.CAPACITY)]
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, item):
        if self.count == Queue.CAPACITY:
            raise Exception("Queue is full")

        self.items[self.rear] = item
        self.rear = (self.rear + 1) % Queue.CAPACITY
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception("Queue is empty")

        item = self.items[self.front]
        self.items[self.front] = 0
        self.front = (self.front + 1) % Queue.CAPACITY
        self.count -= 1
        return item

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.count == Queue.CAPACITY

    def print(self):
        print(self.items)


if __name__ == "__main__":
    q = ArrayQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    q.enqueue(70)
    print(q.dequeue())
    q.enqueue(80)
    q.print()
