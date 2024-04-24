"""
Merge Two Sorted Lists (Easy)
Solved in O(n) time complexity and O(n) space complexity
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        cur = final
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                cur.next = ListNode(list2.val)
                cur = cur.next
                list2 = list2.next
            elif list1.val < list2.val:
                cur.next = ListNode(list1.val)
                cur = cur.next
                list1 = list1.next
            else:
                #theyre equal
                cur.next = ListNode(list1.val)
                cur.next.next = ListNode(list2.val)
                list1 = list1.next
                list2 = list2.next
                cur = cur.next.next

        if list1 != None:
            cur.next = list1
        elif list2 != None:
            cur.next = list2

        return final.next