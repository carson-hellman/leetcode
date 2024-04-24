"""
Roman to Integer (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        total = 0
        key = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i, char in enumerate(s):
            if i != 0:
                if (char == "V" or char == "X") and s[i-1] == "I":
                    total += key[char]
                    total -= (2*key[s[i-1]])
                    continue
                if (char == "L" or char == "C") and s[i-1] == "X":
                    total += key[char]
                    total -= (2*key[s[i-1]])
                    continue
                if (char == "D" or char == "M") and s[i-1] == "C":
                    total += key[char]
                    total -= (2*key[s[i-1]])
                    continue
            
            total += key[char]

        return total