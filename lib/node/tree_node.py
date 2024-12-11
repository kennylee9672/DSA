class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def print(self):
        print(self.value)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)
