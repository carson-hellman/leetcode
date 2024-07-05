"""
Count Good Nodes in Binary Tree (Medium)
Solved in O(n) time complexity and O(1) space complexity
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def path(root, maximum):
            if root is None:
                return 0

            if root.val >= maximum:
                return 1 + path(root.right, max(maximum, root.val)) + path(root.left, max(maximum, root.val))
            else:
                return 0 + path(root.right, max(maximum, root.val)) + path(root.left, max(maximum, root.val))

        return path(root, float('-inf'))