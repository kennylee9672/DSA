'''
https://leetcode.com/problems/merge-two-binary-trees/description/

617. Merge Two Binary Trees

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
'''
from lib.binary_search_tree import BinarySearchTree
from lib.node.tree_node import Node
from typing import Optional


class Solution:
    def mergeTrees(self, root1: Optional[Node], root2: Optional[Node]) -> Optional[Node]:
        merged = None

        def traverse(root1, root2):
            if not root1 or not root2:
                return None

            if root1 and not root2:
                return Node(root1.val)

            if root2 and not root1:
                return Node(root2.val)
            
            print(root1, root2)

            root = Node(root1.value + root2.value)
            root.leftChild = traverse(root1.leftChild, root2.leftChild)
            root.rightChild = traverse(root1.rightChild, root2.rightChild)
        
        traverse(root1, root2)
        return merged

if __name__ == '__main__':
    root1 = BinarySearchTree()
    for x in [1,2,3,5]:
        root1.insert(x)
    
    root2 = BinarySearchTree()
    for x in [2,1,3,4,7]:
        root2.insert(x)
        
    merged = Solution().mergeTrees(root1.root, root2.root)
    print(merged)
    