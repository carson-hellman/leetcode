"""
Longest Square Streak in an Array (Medium)
Solved in O(n log n) time complexity and O(n) space complexity
"""

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 1
        for cur in nums:
            run = 1
            square = cur * cur
            while square in nums:
                run += 1
                square = square * square

            if run > longest:
                longest = run

        if longest == 1:
            return -1
        return longest
