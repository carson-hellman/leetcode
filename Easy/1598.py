"""
Crawler Log Folder (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for operation in logs:
            if operation == "../":
                if depth > 0:
                    depth -= 1
            elif operation == "./":
                continue
            else:
                depth += 1

        return depth