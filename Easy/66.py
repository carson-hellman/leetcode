"""
Plus One (Easy)
Solved in O(n) time complexity and O(n) space complexity
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = 0
        for item in digits:
            output = (output*10) + item

        output += 1


        lst = []
        for item in str(output):
            lst.append(int(item))

        return lst