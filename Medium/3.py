"""
Longest Substring Without Repeating Characters (Medium)
Solved in O(n^2) time complexity and O(n) space complexity
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        if len(s) == 1:
            return 1
        
        for i, letter in enumerate(s):
            seen = set(letter)
            end = i + 1
            while end < len(s) and s[end] not in seen:
                seen.add(s[end])
                end += 1

            if end - i > max_len:
                max_len = end - i

        return max_len