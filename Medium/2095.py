"""
Delete the Middle Node of a Linked List (Medium)
Solved in O(n) time complexity and O(1) space complexity
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur != None:
            count += 1
            cur = cur.next

        if count == 1:
            return None

        if count % 2 == 0:
            mid = (count // 2) + 1
            cur = head
            for i in range(mid - 2):
                cur = cur.next
        else:
            mid = count // 2
            cur = head
            for i in range(mid - 1):
                cur = cur.next

        cur.next = cur.next.next

        return head