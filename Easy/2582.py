"""
Pass the Pillow (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        increasing = 1
        cur = 1
        for i in range(time):
            if increasing == 1:
                if cur == n:
                    increasing = 0
                    cur -= 1
                else:
                    cur += 1
            else:
                # decreasing
                if cur == 1:
                    increasing = 1
                    cur += 1
                else:
                    cur -= 1

            #print(cur)

        return cur