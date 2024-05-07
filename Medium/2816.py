"""
Double a Number Represented as a Linked List (Medium)
Solved in O(n) time complexity and O(n) space complexity
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cur = head
        stack = list()

        while cur != None:
            stack.append(cur)
            cur = cur.next

        while len(stack) > 0:
            cur = stack.pop()
            doubleVal = cur.val * 2
            cur.val = (doubleVal + carry) % 10
            if doubleVal > 9:
                carry = doubleVal // 10
            else:
                carry = 0

        if carry != 0:
            tmp = ListNode(carry, head)
            head = tmp

        return head