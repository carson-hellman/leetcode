"""
Sum Root to Leaf Numbers (Medium)
Solved in O(n) time complexity and O(1) space complexity
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, total):
            if node == None:
                return 0
            total = (total*10) + node.val

            if node.left == None and node.right == None:
                return total
            
            return dfs(node.left, total) + dfs(node.right, total)

        return dfs(root, 0)