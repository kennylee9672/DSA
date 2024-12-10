'''
Charateristics:
    - LIFO (Last In First Out)
    -  Can be implemented with LinkedList/Array

Runtime Complexity:
    - All operations: O(1)
'''
class Stack:
    CAPACITY = 5

    def __init__(self):
        self.count = 0
        self.items = [0 for _ in range(Stack.CAPACITY)]

    def push(self, item):
        if self.count == len(self.items):
            raise Exception("Stack overflow")

        self.items[self.count] = item
        self.count += 1

    def pop(self) -> int:
        if self.isEmpty():
            raise Exception("Null stack pop")

        obj = self.items[self.count - 1]
        self.items[self.count - 1] = 0
        self.count -= 1
        return obj

    def peek(self) -> int:
        if self.isEmpty():
            raise Exception("Null stack peek")

        return self.items[self.count - 1]

    def isEmpty(self):
        return self.count == 0
    
    def print(self):
        print(self.items[:self.count])

if __name__ == "__main__":
    q = Stack()
    q.push(10)
    q.push(20)
    q.push(30)
    print(q.peek())
    q.print()