"""
Insert Greatest Common Divisors in Linked List (Medium)
Solved in O(n log(m)) time complexity where m is the max val in the linked list, and O(1) space complexity
"""

import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        prev = head
        cur = head.next
        while cur != None:
            gcd = math.gcd(prev.val, cur.val)
            node = ListNode(gcd, cur)
            prev.next = node
            prev = cur
            cur = cur.next
        
        return head
        