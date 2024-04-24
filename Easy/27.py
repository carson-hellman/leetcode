"""
Remove Element (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total = 0
        for i in range(len(nums)):
            total += 1
            if nums[i] == val:
                total -= 1
                nums[i] = 999

        nums.sort()
        return total