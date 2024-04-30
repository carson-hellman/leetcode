"""
Reverse Words in a String (Medium)
Solved in O(n) time complexity and O(n) space complexity
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(item for item in reversed(s.strip().split(" ")) if item)