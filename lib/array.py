"""
Time Complexity

Read by Value: O(n)
Read by Index: O(1)
Insertion: O(n) <- copy to new array
Deletion: O(n) <- shift to left

Key Concepts:
- static versus Dynamic
"""


class Array:
    def __init__(self, size: int) -> None:
        self.capacity = size
        self.size = 0
        self.items = [-1 for _ in range(self.capacity)]

    def insert(self, item: int) -> None:
        if self.size == self.capacity:
            self.items = self.items + [-1 for _ in range(self.capacity)]
            self.capacity += self.capacity
        self.items[self.size] = item
        self.size += 1

    def indexOf(self, item: int) -> int:
        for i in range(self.size):
            if self.items[i] == item:
                return i

        return -1

    def removeAt(self, index):
        if index not in range(self.size):
            raise Exception("Index Error")

        for i in range(index, self.size, 1):
            self.items[i] = self.items[i + 1]
        self.size -= 1

    def print(self):
        for it in self.items:
            if it != -1:
                print(it)


nums = Array(3)
nums.insert(10)
nums.insert(20)
nums.insert(30)
nums.insert(40)
print(nums.removeAt(4))
