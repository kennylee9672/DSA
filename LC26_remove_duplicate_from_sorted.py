'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
26. Remove Duplicates from Sorted Array

  j
1 2 2 3 4 4 4 4
    i i+1

    j
1 2 2 3 4 4 4 4
      i i+1
    
        j
1 2 3 4 4 4 4 4
               i i+1
  
  
i=(0,1) -> j.val = (i+1).val, j += 1
i=(2,3) -> j.val = (i+1).val, j += 1
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
      
nums = [1, 1, 1, 2, 2, 3]
k = Solution().removeDuplicates(nums)
print(nums[:k])