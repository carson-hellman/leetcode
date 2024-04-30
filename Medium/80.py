"""
Remove Duplicates from Sorted Array II (Medium)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] and cur < 2:
                count += 1
                cur += 1
                nums[count-1] = nums[i]
            elif nums[i] != nums[i-1]:
                count += 1
                cur = 1
                nums[count-1] = nums[i]

        return count