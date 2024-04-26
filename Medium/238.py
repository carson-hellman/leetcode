"""
Product of Array Except Self (Medium)
Solved in O(n) time complexity and O(n) space complexity
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1 for num in nums]
        postfix = [1 for num in nums]

        # get prefix sum
        for i in range(length):
            if i != 0:
                prefix[i] = prefix[i-1] * nums[i-1]

        # get postfix sum
        for i in range(length-1, -1, -1):
            if i != length-1:
                postfix[i] = postfix[i+1] * nums[i+1]

        return [prefix[i] * postfix[i] for i in range(length)]