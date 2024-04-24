"""
Median of Two Sorted Arrays (Hard)
Solved in O(n log n) time complexity and O(1) space complexity
"""

import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median(nums1 + nums2)