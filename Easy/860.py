"""
Lemonade Change (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        count = 0
        for customer in bills:
            if customer == 5:
                five += 1
            elif customer == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    break
            else: # customer pays with 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    break

            count += 1
        return count == len(bills)
