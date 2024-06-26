"""
Eliminate Maximum Number of Monsters (Medium)
Solved in O(n) time complexity and O(n) space complexity
"""

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        timeToCity = [dist[i] / speed[i] for i in range(len(dist))]
        timeToCity.sort()

        for i in range(len(timeToCity)):
            if timeToCity[i] <= i:
                return i

        return len(dist)