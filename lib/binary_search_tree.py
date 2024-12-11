from lib.node.tree_node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return

        curr = self.root
        while True:
            if value < curr.value:
                if not curr.leftChild:
                    curr.leftChild = node
                    break
                curr = curr.leftChild
            else:
                if not curr.rightChild:
                    curr.rightChild = node
                    break
                curr = curr.rightChild

    def find(self, value) -> bool:
        curr = self.root
        while curr:
            if value < curr.value:
                curr = curr.leftChild
            elif value > curr.value:
                curr = curr.rightChild
            else:
                return True
        return False

    def __repr__(self):
        return str(self.root.value)

    def __str__(self):
        return str(self.root.value)


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(7)
    tree.insert(4)
    tree.insert(9)
    tree.insert(1)
    tree.insert(6)
    tree.insert(8)
    tree.insert(10)

    print(tree.find(3))
    print(tree.find(10))

    print("End")
