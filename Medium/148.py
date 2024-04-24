"""
Sort List (Medium)
Solved in O(n) time complexity and O(n) space complexity
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = []

        if head == None:
            return head

        while head != None:
            s.append(head.val)
            head = head.next

        s.sort()
        print(s)
        head = ListNode(val = s[0])
        initialHead = head
        for i in range(1, len(s)):
            head.next = ListNode(s[i])
            head = head.next

        return initialHead