"""
Three consecutive odds (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consec = 0
        for item in arr:
            if item % 2 != 0:
                consec += 1
            else:
                consec = 0

            if consec == 3:
                return True

        return False