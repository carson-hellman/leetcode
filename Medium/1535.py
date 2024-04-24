"""
Find the Winner of an Array Game (Medium)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        if k >= len(arr):
            return max(arr)

        consecutive = 0
        winner = arr[0]
        while consecutive < k:
            if arr[0] > arr[1]:
                consecutive += 1
                tmp = arr.pop(1)
                arr.append(tmp)
            else:
                winner = arr[1]
                consecutive = 1
                arr.append(arr.pop(0))

        return winner