'''
- Breadth First (Level Order): 20, 10, 30, 6, 14, 24, 3, 8, 26
- Depth First
- Pre-order: 20, 10, 6, 3, 8, 14, 30, 24, 26
- In-order: 3, 6, 8, 10, 14, 20, 24, 26, 30
- Post-order: 3, 8, 6, 14, 10, 26, 24, 30, 20
'''
from lib.binary_search_tree import BinarySearchTree
from lib.node.tree_node import Node


class Traverser:
    def __init__(self, tree: BinarySearchTree):
        self.root = tree.root

    # root, left, right
    def preOrder(self):
        result = []

        def visit(node: Node):
            if not node:
                return

            result.append(node.value)
            visit(node.leftChild)
            visit(node.rightChild)

        visit(self.root)
        return result

    # left, root, right
    def inOrder(self):
        result = []

        def visit(node: Node):
            if not node:
                return

            visit(node.leftChild)
            result.append(node.value)
            visit(node.rightChild)

        visit(self.root)
        return result

    # left, right, root
    def postOrder(self):
        result = []

        def visit(node: Node):
            print('Visting: ', node)
            if not node:
                return None

            if Traverser.isLeafNode(node):
                return node.value

            left = visit(node.leftChild)
            if left:
                result.append(left)
            right = visit(node.rightChild)
            if right:
                result.append(right)
            result.append(node.value)

        visit(self.root)
        return result

    def breadthFirstSearch(self):
        result = []
        q = [self.root]
        while q:
            n = q.pop()
            result.append(n.value)
            if n.leftChild:
                q.append(n.leftChild)
            if n.rightChild:
                q.append(n.rightChild)
        return result

    def height(self) -> int:
        def _height(node) -> int:
            if not node:
                return -1

            h1 = _height(node.leftChild)
            h2 = _height(node.rightChild)
            return 1 + max(h1, h2)
        return _height(self.root)

    def minNode(self) -> int:
        def _minNode(n: Node) -> int:
            # Is leaf node
            if not (n.leftChild and n.rightChild):
                return n.value

            left = _minNode(n.leftChild)
            right = _minNode(n.rightChild)
            return min(n.value, min(left, right))

        return _minNode(self.root)

    def equals(self, tree: BinarySearchTree) -> bool:
        if not tree:
            return False

        def _equals(n1: Node, n2: Node):
            if not n1 and not n2:
                return True

            if n1 and n2:
                return (n1.value == n2.value) \
                    and _equals(n1.leftChild, n2.leftChild) \
                    and _equals(n1.rightChild, n2.rightChild)

            return False

        return _equals(self.root, tree.root)

    def validBST(self) -> bool:
        import math

        def _validBST(n: Node, lower, uppper):
            if not n:
                return True

            # Basic Validation
            if not (n.value > lower and n.value < uppper):
                return False

            return _validBST(n.leftChild, lower, n.value) \
                and _validBST(n.rightChild, n.value, uppper)

        return _validBST(self.root, -math.inf, math.inf)

    def printNodesAtDistanceK(self, k):
        def _printNodesAtDistanceK(n: Node, k):
            if not n:
                return

            if k == 0:
                print(n.value)
                return

            _printNodesAtDistanceK(n.leftChild, k - 1)
            _printNodesAtDistanceK(n.rightChild, k - 1)

        _printNodesAtDistanceK(self.root, k)

    def BFS(self):
        result = {}

        def _BFS(n, h1, h2) -> int:
            if not n:
                return

            height = 1 + max(h1, h2)
            if height not in result:
                result[height] = []

            result[height].append(n.value)
            _BFS(n.leftChild, height + 1, height)
            _BFS(n.rightChild, height, height + 1)

        _BFS(self.root, -1, -1)
        for height in result:
            print(result[height])

    def swap(self):
        tmp = self.root.leftChild
        self.root.leftChild = self.root.rightChild
        self.root.rightChild = tmp

    @staticmethod
    def isLeafNode(n: Node):
        return not n.leftChild and not n.rightChild
