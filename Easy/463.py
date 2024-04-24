"""
Island Perimeter (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimiter = 0

        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1:
                    perimiter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimiter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimiter -= 2

        return perimiter