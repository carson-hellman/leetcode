"""
Remove Duplicates from Sorted Array (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        count = 0
        for i, item in enumerate(nums):
            if item in unique:
                nums[i] = 1000
            else:
                unique.add(item)
                count += 1

        nums.sort()
        return len(unique)
        