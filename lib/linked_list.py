"""
Runtime Complexity

- Lookup:
    - Head/Tail: O(1), O(n) otherwise
- Insertion:
    - Head/Tail: O(1), O(n) otherwise
- Deletion:
    - Head: O(1)
    - Tail/Middle: O(n)
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.__size = 0

    def addFirst(self, val):
        node = Node(val)
        if self.__isEmpty():
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node
        self.__size += 1

    def addLast(self, val):
        node = Node(val)
        if self.__isEmpty():
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.__size += 1

    def removeFirst(self):
        if self.__isEmpty():
            raise AttributeError

        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            second = self.first.next
            self.first.next = None
            self.first = second
        self.__size -= 1

    def removeLast(self):
        if self.__isEmpty():
            return AttributeError

        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            prev = self.__getPrevious(self.last)
            prev.next = None
            self.last = prev
        self.__size -= 1

    def contains(self, val):
        return self.indexOf(val) != -1

    def indexOf(self, val):
        i = 0
        curr = self.first
        while curr:
            if curr.val == val:
                return i
            i += 1
            curr = curr.next
        return -1

    def size(self):
        return self.__size

    def print(self):
        print(self.toArray())

    def toArray(self):
        i = 0
        curr = self.first
        nums = []
        while curr:
            nums.append(curr.val)
            i += 1
            curr = curr.next
        return nums

    def reverse(self):
        prev = None
        curr = self.first
        while curr:
            print(curr.val)
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.last = self.first
        self.first = prev

    def __isEmpty(self):
        return self.first == None

    def __getPrevious(self, node):
        curr = self.first
        while curr:
            if curr.next == node:
                return curr
            curr = curr.next
        return None


if __name__ == "__main__":
    lst = LinkedList()
    lst.addLast(10)
    lst.addLast(20)
    # lst.addLast(30)
    lst.print()

    lst.reverse()
    lst.print()
