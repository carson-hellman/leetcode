"""
Average Waiting Time (Medium)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalWait = 0
        prevStart = 0
        prevDuration = 0
        for i in customers:
            if prevStart + prevDuration < i[0]:
                # no wait
                prevStart = i[0]
                prevDuration = i[1]
                totalWait += i[1]
            else:
                # wait
                totalWait += (prevStart + prevDuration + i[1]) - i[0]
                prevStart = max(prevStart + prevDuration, i[0])
                prevDuration = i[1]

        return totalWait / len(customers)