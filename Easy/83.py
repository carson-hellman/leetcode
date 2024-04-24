"""
Remove Duplicates from Sorted List (Easy)
Solved in O(n) time complexity and O(1) space complexity
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev = head
        cur = head.next

        while cur != None:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
                continue

            prev = cur
            cur = cur.next

        return head