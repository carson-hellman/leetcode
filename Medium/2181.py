"""
Merge Nodes in Between Zeros (Medium)
Solved in O(n) time complexity and O(1) space complexity
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        merge = None
        cur = head

        while cur != None:
            if cur.val == 0:
                if merge != None:
                    merge.next = cur
                if cur.next != None:
                    merge = cur

            merge.val += cur.val
            cur = cur.next

        merge.next = None

        return head
