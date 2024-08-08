"""
Spiral Matrix III (Medium)
Solved in O(rows*cols) time complexity and O(n) space complexity
"""

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        output = []
        curRow = rStart
        curCol = cStart
        step = 1
        total = rows * cols
        while len(output) < total:
            # check initial index
            if step == 1:
                if (0 <= curRow < rows) and (0 <= curCol < cols):
                    output.append([curRow, curCol])

            # increment and check next cols
            for c in range(curCol+1, curCol+step+1):
                if (0 <= curRow < rows) and (0 <= c < cols):
                    output.append([curRow, c])
            curCol += step

            # increment and check next rows
            for r in range(curRow+1, curRow+step+1):
                if (0 <= r < rows) and (0 <= curCol < cols):
                    output.append([r, curCol])
            curRow += step
            
            # increase step distance
            step += 1
            
            # decrement and check next cols
            for c in range(curCol-1, curCol-step-1, -1):
                if (0 <= curRow < rows) and (0 <= c < cols):
                    output.append([curRow, c])
            curCol -= step

            # decrement and check next rows
            for r in range(curRow-1, curRow-step-1, -1):
                if (0 <= r < rows) and (0 <= curCol < cols):
                    output.append([r, curCol])
            curRow -= step
        
            # increase step distance
            step += 1

        return output