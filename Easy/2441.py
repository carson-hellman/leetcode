"""
Largest Positive Integer That Exists With Its Negative (Easy)
Solved in O(n lg n) time complexity and O(1) space complexity
"""

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        neg = 0
        pos = len(nums) - 1
        while neg != pos:
            lower = nums[neg] * -1
            upper = nums[pos]
            if lower == upper:
                return upper
            elif lower > upper:
                neg += 1
            else:
                pos -= 1

        return -1