"""
Valid Parentheses (Easy)
Solved in O(n) time complexity and O(n) space complexity
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False

        pairs = {"(":")", "[":"]", "{":"}"}
        stack = list()

        for item in s:
            if item in "([{":
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                    
                check = stack.pop()
                if pairs[check] != item:
                    return False

        if len(stack) != 0:
            return False

        return True