"""
Two Sum II - Input Array Is Sorted (Medium)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers)-1
        
        while idx1 < idx2:
            cur = numbers[idx1] + numbers[idx2]
            if cur == target:
                return [idx1+1, idx2+1]
            elif cur < target:
                idx1 += 1
            else:
                idx2 -= 1