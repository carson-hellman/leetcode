"""
Top K Frequent Elements (Medium)
Solved in O(n) time complexity and O(n^2) space complexity
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        output = list()
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        keys = list(counter.keys())
        vals = list(counter.values())

        for i in range(k):
            index = vals.index(max(vals))
            output.append(keys[index])
            keys.pop(index)
            vals.pop(index)

        return output