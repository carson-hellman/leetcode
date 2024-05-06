"""
Add two numbers (Medium)
Solved in O(n) time complexity and O(n) space complexity
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curOne = l1
        curTwo = l2
        carry = 0
        output = ListNode()
        tail = output
        while curOne != None and curTwo != None:
            sumNums = curOne.val + curTwo.val + carry
            print(sumNums)
            if sumNums > 9:
                carry = sumNums // 10
            else:
                carry = 0

            tail.next = ListNode(sumNums % 10)
            tail = tail.next
            curOne = curOne.next
            curTwo = curTwo.next

        if curOne == None:
            while curTwo != None:
                val = curTwo.val + carry
                if val > 9:
                    carry = val // 10
                else:
                    carry = 0

                tail.next = ListNode(val % 10)
                tail = tail.next
                curTwo = curTwo.next


        if curTwo == None:
            while curOne != None:
                val = curOne.val + carry
                if val > 9:
                    carry = val // 10
                else:
                    carry = 0

                tail.next = ListNode(val % 10)
                tail = tail.next
                curOne = curOne.next

        if carry != 0:
            tail.next = ListNode(carry)
            
        return output.next