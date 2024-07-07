"""
Water Bottles (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            total += 1
            numBottles -= numExchange
            numBottles += 1

        return total