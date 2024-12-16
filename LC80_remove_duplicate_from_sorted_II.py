'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
80. Remove Duplicates from Sorted Array II

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count = 1
            else:
                count += 1

            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j

nums = [1, 1, 1, 2, 2, 3]
k = Solution().removeDuplicates(nums)
print(nums)
print(nums[:k])
