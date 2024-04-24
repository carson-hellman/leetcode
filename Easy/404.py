"""
Sum of Left Leaves (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, left):
            if node == None:
                return 0
                
            if node.left == None and node.right == None:
                if left == 1:
                    return node.val
                return 0
    
            return dfs(node.left, 1) + dfs(node.right, 0)

        return dfs(root, 0)