"""
Merge Strings Alternately (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        len1 = len(word1)
        len2 = len(word2)

        end = 0
        for i in range(min(len1,len2)):
                merged = merged + word1[i] + word2[i]
                end = i+1
        return merged + word1[end:] + word2[end:]
