"""
Find the Minimum and Maximum Number of Nodes Between Critical Points (Medium)
Solved in O(n) time complexity and O(1) space complexity
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [float("inf"), -1]
        prev = None
        cur = head
        curMinLen = 0
        curMaxLen = 0
        firstCritical = 0

        while cur.next != None:
            if prev == None:
                prev = cur
                cur = cur.next
                continue
            
            if firstCritical == 1:
                curMaxLen += 1
                curMinLen += 1

            if (prev.val < cur.val and cur.val > cur.next.val) or (prev.val > cur.val and cur.val < cur.next.val):
                # critical point
                if firstCritical == 0:
                    # is first critical point: begin counting
                    firstCritical = 1
                
                if curMaxLen > result[1] and curMaxLen != 0:
                    # new long distance between critical points
                    result[1] = curMaxLen

                if firstCritical == 1:
                    # check min distances
                    if curMinLen < result[0] and curMinLen != 0:
                        result[0] = curMinLen

                    curMinLen = 0

            prev = cur
            cur = cur.next 

        if result[0] == float('inf'):
            result[0] = -1

        return result       
            