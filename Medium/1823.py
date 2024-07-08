"""
Find the Winner of the Circular Game (Medium)
Solved in O(n^2 * k) time complexity and O(n) space complexity
"""
### NOTE: could be solved in O(n*k) time complexity using a deque instead of a list for the queue

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1, n+1)]

        while (len(circle) > 1):
            for i in range(k-1):
                cur = circle.pop(0)
                circle.append(cur)

            delete = circle.pop(0)
            #print(delete)

        return circle[0]
