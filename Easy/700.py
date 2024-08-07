"""
Search in a Binary Search Tree (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root

        while cur != None:
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                cur = cur.right
            else:
                return cur