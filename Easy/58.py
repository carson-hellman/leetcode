"""
Length of Last Word (Easy)
Solved in O(n) time complexity and O(n) space complexity
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        check = s.strip().split(" ")
        return len(check[-1])