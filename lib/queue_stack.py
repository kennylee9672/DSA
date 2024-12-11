from queue import Queue
from stack import Stack


class StackQueue(Queue):
    def __init__(self):
        self.count = 0
        self.enq = Stack()
        self.deq = Stack()

    def enqueue(self, it):
        if self.isFull():
            return

        self.enq.push(it)
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return -1

        StackQueue.moveToQueue(self.enq, self.deq)
        return self.deq.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        
        StackQueue.moveToQueue(self.enq, self.deq)
        return self.deq.peek()

    @staticmethod
    def moveToQueue(q1, q2):
        if q2.isEmpty():
            while not q1.isEmpty():
                q2.push(q1.pop())

    def isEmpty(self):
        return self.enq.isEmpty() and self.deq.isEmpty()

    def isFull(self):
        return self.count == Queue.CAPACITY
    
    def print(self):
        print('------ My Queue ------')
        self.enq.print()
        self.deq.print()
        print('-------- End ---------')

if __name__ == "__main__":
    q = StackQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.print()

    q.dequeue()
    q.dequeue()
    q.print()
    
    q.enqueue(40)
    q.enqueue(50)
    q.print()
    
    print(q.dequeue())
    print(q.dequeue())
    # print(q.dequeue())
    # q.enqueue(80)
    