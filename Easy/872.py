"""
Leaf-Similar Trees (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(root):
            if root.left == None and root.right == None:
                return [root.val]
            elif root.left == None:
                return getLeaves(root.right)
            elif root.right == None:
                return getLeaves(root.left)
            else:
                return getLeaves(root.left) + getLeaves(root.right)

        return getLeaves(root1) == getLeaves(root2)