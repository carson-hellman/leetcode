"""
Group Anagrams (Medium)
Solved in O(n) time complexity and O(1) space complexity
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = dict()
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword in anagrams:
                anagrams[sortedword].append(word)
            else:
                anagrams[sortedword] = [word]

        return anagrams.values()