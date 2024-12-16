class Node:
    def __init__(self, label):
        self.label = label

    def print(self):
        print(self.label)

    def __repr__(self):
        return str(self.label)

    def __str__(self):
        return str(self.label)
