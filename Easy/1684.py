"""
Count the Number of Consistent Strings (Easy)
Solved in O(n * k) time complexity and O(m) space complexity
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        check = set(allowed)
        total = 0
        for word in words:
            valid = True
            for letter in word:
                if letter not in check:
                    valid = False
                    break
            if valid == True:
                total += 1

        return total

                
