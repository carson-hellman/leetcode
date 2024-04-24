"""
Find the Index of the First Occurrence in a String (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for start in range(len(haystack)):
            if haystack[start] == needle[0]:
                if haystack[start:start+length] == needle:
                    return start
        
        return -1