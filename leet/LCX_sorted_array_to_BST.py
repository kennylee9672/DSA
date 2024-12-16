'''
108. Convert Sorted Array to Binary Search Tree

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
'''
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'Node: {self.val}'


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def traverse(left, right):
            if left > right:
                return None

            mid = (right - left) // 2 + left
            root = TreeNode(val=nums[mid])
            root.left = traverse(left, mid - 1)
            root.right = traverse(mid + 1, right)
            return root

        return traverse(0, len(nums) - 1)

nums = [-10,-3,0,5,9]
root = Solution().sortedArrayToBST(nums)
print()