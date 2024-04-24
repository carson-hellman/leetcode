"""
Search Insert Position (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if target == num:
                return i
            if target < num:
                return i
        
        return len(nums)